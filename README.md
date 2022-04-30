# vue-django-rest

## LOCAL UP
### Setup
`pip3 install -r requirements.txt`

`cd djangoapp`

`python3 manage.py makemigrations myapp`

`python3 manage.py migrate`

### python server
`cd djangoapp`

`python3 manage.py runserver`

### vue server
`cd vueapp`

`npm install`

`npm run serve`


## DOCKER UP

### Setup
`pip3 install -r requirements.txt`

`cd djangoapp`

`python3 manage.py makemigrations myapp`

`python3 manage.py migrate`

### Docker build

`docker-compose build`

### Docker run

`docker-compose up -d`
