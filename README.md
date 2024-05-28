### Adam's website

poetry self update
poetry init
poetry shell
poetry install

poetry export -f requirements.txt --without-hashes --without-urls --output requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser