from django.core.management import BaseCommand

from accounts.factories import UserFactory


class Command(BaseCommand):
    help = 'fake a number of active users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=5,
            help='amount of user to create'
        )

    def handle(self, *args, **options):
        users = UserFactory.create_batch(options['count'])

        self.stdout.write(self.style.SUCCESS(
            f'{len(users)} user(s) successfully created.'
        ))

        for user in users:
            self.stdout.write(self.style.SUCCESS(
                f'{user.get_full_name()}: {user.email}, {UserFactory.plain_password}'
            ))
