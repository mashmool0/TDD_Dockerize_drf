#!/bin/sh

if [" $DATABASE$"= "postgres"]
then
    echo "waiting for postgres..."


    while ! nc -z $SQL_HOST$ $SQL_PORT$;do
        sleep 0.1
    done 

    echo "PostgreSQL started" 

fi 

python movie_project/manage.py flush -no--input
python movie_project/manage.py migrate 


exec "$@"