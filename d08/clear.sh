#!/bin/sh

rm -rf db.sqlite3
rm -rf */__pycache__
pip3 uninstall django-ex-module
rm -rf staticfiles
rm -rf mediafiles
rm -rf d08.sock
rm -rf /Users/bledda/.brew/etc/nginx/servers/nginx_django.conf
rm -rf d08.log