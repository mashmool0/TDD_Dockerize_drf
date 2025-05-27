#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Run migrations
python movie_project/manage.py makemigrations
python movie_project/manage.py migrate

# Collect static files in production
if [ "$DJANGO_ENVIRONMENT" = "production" ]; then
    echo "Collecting static files..."
    python movie_project/manage.py collectstatic --no-input
fi

exec "$@"
