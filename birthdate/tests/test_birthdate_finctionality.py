from django.test import TestCase
from ..get_disney_info import open_csv, get_movie_id, get_movie_info, get_nearest_movie_by_date
from ..views import convert_to_int
from pandas import DataFrame


class BirthdateIntakeFunctionalityTest(TestCase):
    def setUp(self):
        self.birthyear = '1992'
        self.birthmonth = '09'
        self.birthday = '16'
        self.data = {
            'birthyear': self.birthyear,
            'birthmonth': self.birthmonth,
            'birthday': self.birthday
        }

    def test_05_convert_to_int_pass(self):
        converted_dict = convert_to_int(**self.data)
        self.assertIsInstance(converted_dict, dict)

    def test_10_convert_to_int_fail(self):
        self.data['birthday'] = 'NOT AN INT'
        with self.assertRaises(ValueError):
            convert_to_int(**self.data)

    def test_15_open_csv_pass(self):
        df = open_csv(path='disney-characters.csv')
        self.assertIsInstance(df, DataFrame)

    def test_20_open_csv_fail(path):
        with self.assertRaises(FileNotFoundError):
            open_csv('NONEXISTENT_PATH.csv')
