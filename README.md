# Disney Movie Finder
#### Find which Disney movie was released nearest to your birthday

Enjoy wasting time with those "Find out which Hogwarts House you'd be placed" type of personality tests? Me too! Ever wonder which Disney film was was the newest talk of the town you were a baby? Me too!

## Description
This simple API takes in birthyear, birthmonth, and birthday from the query parameters to determine which Disney movie was released nearest to your birthday. The application then sends a request to the IMDB-API to get further details on the movie. Finally, a json response is sent back to the user with the movie tital, runtime, and a plot description.

## Getting Started

### Dependencies
I use the following technologies:
* Windows Substem for Linux (WSL2)
    - running Ubuntu 20.04
* pipenv, version 2021.5.29
* python3, version 3.8.10

### Installing
* start and activate a new python environment
    - pipenv shell
* install dependencies
    - pipenv install

### Executing program
* create an .env file in the 'ddisney_movie_finder' main project folder (along side the settings.py)
    - *the application will not work without the environment variables!*
    - credentials will be sent via email
* to start the application:
    - ```python3 manage.py runserver```
    - Note: you will see a warning about unapplied migrations. These can be safely ignored since this application does not use a database and does not utilize Django's ORM.
* to run tests:
    - ```python3 manage.py test```

## Endpoint
After starting the server, travel to /api/birthdate/?birthyear=[INSERT YOUR BIRTH YEAR]>&birthmonth=[INSERT YOUR BIRTH MONTH]&birthday[INSERT YOUR BIRTHDAY]
* Example:
http://127.0.0.1:8000/api/birthdate/?birthyear=1991&birthmonth=10&birthday=10
* Returns: JSON response with nearest movie's runtime, title, and plot on success.

## Authors
Debra Sparr
[Email](dsparr1010@gmail.com)


## Version History
* 0.1
    * Initial Release


## Acknowledgments
* [Disney Character Dataset](https://data.world/kgarrett/disney-character-success-00-16)
    - [@kgarrett](https://data.world/kgarrett)
* [IMDB API](https://developer.imdb.com/)
* [All contributors of open source projects](https://quotefancy.com/media/wallpaper/3840x2160/6964-Isaac-Newton-Quote-If-I-have-seen-further-it-is-by-standing-on-the.jpg)
