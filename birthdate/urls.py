from django.urls import path, include
from .views import birthdate


app_name = 'api'

# <str:birthyear><str:birthmonth><str:birthday>

urlpatterns = [
    path('birthdate/',
         birthdate, name='birthdate')
]
