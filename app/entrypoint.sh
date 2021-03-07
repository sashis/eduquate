#!/bin/bash

if [[ $DB_ENGINE =~ postgres ]]
then
    echo "Waiting for postgres..."
    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py createadmin --email $ADMIN_EMAIL --password $ADMIN_PASSWORD
python manage.py fill_test_db

exec "$@"
