from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class StatusCodesTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_05_birthdate_success(self):
        res = self.client.get('/api/birthdate/', {
            'birthyear': '1991', 'birthmonth': '10', 'birthday': '10'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_10_birthdate_nonint_fail(self):
        res = self.client.get('/api/birthdate/', {
            'birthyear': '199g', 'birthmonth': '1n', 'birthday': 'n8'})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_15_birthdate_length_fail(self):
        res = self.client.get('/api/birthdate/', {
            'birthyear': '1992', 'birthmonth': '090', 'birthday': '16'})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_20_birthdate_all_null_value_fail(self):
        res = self.client.get('/api/birthdate/', {
            'birthyear': '', 'birthmonth': '', 'birthday': ''})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_20_birthdate_one_null_value_fail(self):
        res = self.client.get('/api/birthdate/', {
            'birthyear': '1992', 'birthmonth': '09', 'birthday': ''})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_20_birthdate_no_parameters_fail(self):
        res = self.client.get('/api/birthdate/')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
