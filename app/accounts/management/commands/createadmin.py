from django.core.management import BaseCommand

from accounts.models import User


class Command(BaseCommand):
    help = 'create superuser with no input'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, help='admin email')
        parser.add_argument('--password', type=str, help='admin password')

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']
        admin = User.objects.create_superuser(email, password)
        self.stdout.write(self.style.SUCCESS(
            f'Superuser {admin} created.'
        ))
