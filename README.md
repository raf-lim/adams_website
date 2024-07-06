### Adam's website

poetry self update
poetry init
poetry shell
poetry install

#### local development requirements.txt
poetry export -f requirements.txt --with dev --with test --without-hashes --without-urls --output compose/local/requirements.txt

#### production requirements.txt
poetry export -f requirements.txt without dev --without test --with-hashes --without-urls --output compose/production/requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser