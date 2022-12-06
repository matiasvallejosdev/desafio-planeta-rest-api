#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# How to automate createsuperuser on django
# https://stackoverflow.com/questions/6244382/how-to-automate-createsuperuser-on-django/59467533#59467533
python manage.py collectstatic --no-input
python manage.py migrate

