import pandas as pd
import os
import requests
from datetime import datetime


KEY = os.getenv('IMDB_KEY')


def open_csv(path: str = 'disney-characters.csv'):
    ''' Opens the CSV file in root with Pandas, formats, and returns a Dataframe '''
    try:
        with open(path)as csv_file:
            df = pd.read_csv(csv_file, header=0, engine='python',
                             encoding='utf8', dtype={'release_date': 'datetime64'})
            df = df.dropna()
            df = df.replace('\n', '', regex=True)
            df = df.set_index('release_date')
            return df
    except FileNotFoundError:
        raise FileNotFoundError('csv file must be in the root directory')
    finally:
        csv_file.close()


def get_nearest_movie_by_date(year: int, month: int, day: int, df=open_csv()):
    ''' Finds movie with nearest release date to given date and returns a Series '''
    return df.iloc[df.index.get_loc(
        datetime(year, month, day), method='nearest')]


def get_movie_id(nearest_movie) -> str:
    ''' Sends request to IMDB API and returns found movie's ID '''
    imdb_id = None
    movie_year = nearest_movie.name.date().year
    r = requests.get(
        f'https://imdb-api.com/en/API/SearchMovie/{KEY}/{nearest_movie.movie_title}')
    if r.status_code != 200:
        raise ConnectionError('Issue sending request to imdp-api')
    res = r.json()
    for x in res['results']:
        if str(movie_year) in x['description']:
            imdb_id = x['id']
    return imdb_id


def get_movie_info(imdb_id: str) -> dict:
    ''' Gets details on a movie and returns the details '''
    r = requests.get(
        f'https://imdb-api.com/en/API/Title/{KEY}/{imdb_id}')
    if r.status_code != 200:
        raise ConnectionError('Issue sending request to imdp-api')
    res_dict = r.json()
    data = {
        'runtime': res_dict['runtimeStr'],
        'desc': res_dict['plot'],
        'img': res_dict['image']
    }
    return data
