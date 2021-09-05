import pandas as pd
import os
import json
import requests
from datetime import datetime
# dev
from pprint import pprint


QP_EXAMPLE = {
    'birth_year': '1991',
    'birth_month': '10',
    'birth_day': '10',
    'first_name': 'Debra'
}


KEY = 'k_3ed1lbo4'


def main():
    with open('disney-characters.csv')as csv_file:
        df = pd.read_csv(csv_file, header=0, engine='python',
                         encoding='utf8', dtype={'release_date': 'datetime64'})
        # df = df.dropna()
        df = df.replace('\n', '', regex=True).dropna()
        df = df.set_index('release_date')
        # df = df.reset_index(drop=True)

        # print(df)
        # print(type(df['release_date'][0]))
        # check = df.iloc[df.index.get_loc(
        #     datetime(int(QP_EXAMPLE['birth_year']), int(QP_EXAMPLE['birth_month']), int(QP_EXAMPLE['birth_day'])), method='nearest')]

        check = df.iloc[df.index.get_loc(
            datetime(1991, 10, 10), method='nearest')]
        movie_year = check.name.date().year

        r = requests.get(
            f'https://imdb-api.com/en/API/SearchMovie/{KEY}/{check.movie_title}')
        res1 = json.loads(r.text)
        imdb_id = None
        for x in res1['results']:
            if str(movie_year) in x['description']:
                print(x)
                imdb_id = x['id']

        if imdb_id:
            r2 = requests.get(
                f'https://imdb-api.com/en/API/Title/{KEY}/{imdb_id}')
            r2_dict = r2.json()
            data = {
                'runtime': r2_dict['runtimeStr'],
                'desc': r2_dict['plot'],
                'img': r2_dict['image']
            }
            print(data)


if __name__ == '__main__':
    main()
