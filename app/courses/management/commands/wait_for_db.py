import time

from django.db import connection
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Waits for database being available.'

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available!'))
