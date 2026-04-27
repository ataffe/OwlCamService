#!/bin/sh
echo "Waiting for postgres..."
until pg_isready -h "$DATABASE_HOST" -p "$DATABASE_PORT" -U "$DATABASE_USERNAME"; do
    sleep 1
done
echo "Postgres is ready."

python manage.py migrate --noinput
exec gunicorn --bind 0.0.0.0:8000 --workers 3 owlcamservice.wsgi:application
