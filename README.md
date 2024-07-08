### Adam's website
https://adams.up.railway.app/

Simple CRUD application for storing information about aircrafts and games developed for a 10 year old kid with Django framework. Most of commented lines in the code are left intentionally for possible use in the future.

### To run the project in development mode:
Clone the repository for github.com
```command
git clone https://github.com/raf-lim/adams_website
```
It is dockerized so compose the image and run containers:
```command
docker compose up -d
```
The app should be now running on http://localhost:8000. To be able to add regular items you need to be loggedin as standard user. To add/modify app's items you need to be a superuser. Signing up is turned off so the superuser needs to register a standard user (or another superuser). To create first superuser, in docker's CLI:
```command
python manage.py createsuperuser
```
Now you can now add more users (or superusers) in admin panel http://localhost:8000/admin/


### Poetry is used to manage dependencies.
https://python-poetry.org/docs/basic-usage/

To create local environment (Poetry should be installed):
```command
poetry self update
poetry init
poetry shell
poetry install
```
To update current dependencies:
```command
poetry update
```
and:

#### for local development
```command
poetry export -f requirements.txt --with dev --with test --without-hashes --without-urls --output compose/local/requirements.txt
```
```command
docker compose up --build -d
```

#### for production
```command
poetry export -f requirements.txt without dev --without test --without-urls --output compose/production/requirements.txt
```

### Testing
As the project is mainly based on generic models, besides users app it is not tested. It may come in the future.

In docker's CLI root:
```command
pytest
```
To see the coverage:
```command
coverage run -m pytest
coverage html
```
open htmlcov/index.html in a browser.

Typing checks with mypy:

```command
mypy mysite
```
