#!/bin/bash

if [[ $EDUQUATE_DB_ENGINE =~ postgres ]]
then
    echo "Waiting for postgres..."
    while ! nc -z $EDUQUATE_DB_HOST $EDUQUATE_DB_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py createadmin --email $EDUQUATE_ADMIN_EMAIL --password $EDUQUATE_ADMIN_PASSWORD
python manage.py fill_test_db

exec "$@"
