from django.urls import path, include
from .views import birthdate


app_name = 'api'

urlpatterns = [
    path('birthdate/',
         birthdate, name='birthdate')
]
