#!/bin/sh

/usr/sbin/nginx -c /app/nginx.conf

/usr/local/bin/gunicorn -c /app/gunicorn_conf.py web.wsgi:application

