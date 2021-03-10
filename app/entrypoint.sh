#!/bin/bash

python manage.py wait_for_db

if [ $MAIN_APP ]
then
    python manage.py flush --no-input
    python manage.py migrate
    python manage.py createadmin --email $ADMIN_EMAIL --password $ADMIN_PASSWORD
    python manage.py fill_test_db
fi

exec "$@"
