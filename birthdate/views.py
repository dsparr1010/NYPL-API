from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from .get_disney_info import open_csv, get_movie_id, get_movie_info, get_nearest_movie_by_date


def convert_to_int(**kwargs) -> dict:
    ''' Converts a dictionary's values to integers and returns a new dictionary '''
    try:
        return {key: int(value) for (key, value) in kwargs.items()}
    except ValueError:
        raise ValueError('All values must be an integer')


def find_movie_info(**data) -> dict:
    nearest_movie = get_nearest_movie_by_date(
        year=data['birthyear'], month=data['birthmonth'], day=data['birthday'])
    movie_id = get_movie_id(nearest_movie)
    if not movie_id:
        raise ValueError('Result for movie not found')
    return get_movie_info(movie_id)


@api_view(['GET'])
def birthdate(request):
    try:
        data = {
            'birthyear': request.query_params.get('birthyear', None),
            'birthmonth': request.query_params.get('birthmonth', None),
            'birthday': request.query_params.get('birthday', None)
        }

        if not all(data.values()):
            raise ValueError(
                'birthyear, birthmonth, and birthday are required fields')
        if len(data['birthyear']) != 4 or len(data['birthmonth']) != 2 or len(data['birthday']) != 2:
            raise ValueError(
                'YYYY-mm-dd format expected (i.e. birthyear=1991&birthmonth=10&birthday=10)')

        formatted_data = convert_to_int(**data)

        disney_movie_desc = find_movie_info(**formatted_data)
        return JsonResponse(disney_movie_desc, status=200)
    except (ValueError, ConnectionError) as err:
        return JsonResponse({'status': 400, 'type': type(err).__name__, 'msg': err.__str__()}, status=400)
