#!/bin/sh

uwsgi --socket d08.sock --wsgi-file ./d08/wsgi.py --chmod-socket=666 --daemonize=/Users/bledda/d08/d08.log
