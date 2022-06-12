#!/bin/sh

pip3 install -r requirements.txt
python3 manage.py makemigrations ex_module
python3 manage.py migrate
python3 manage.py collectstatic
export DJANGO_SETTINGS_MODULE=d08.settings
