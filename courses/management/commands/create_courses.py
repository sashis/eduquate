from django.core.management import BaseCommand

from ...factories import generate_course_with_lessons


class Command(BaseCommand):
    help = 'fake a number of courses with lessons'

    def add_arguments(self, parser):
        parser.add('--courses', type=int, default=10, help='course count')
        parser.add('--lessons', type=int, default=10, help='lesson count per course')

    def handle(self, *args, **options):
        course_cnt = options['courses']
        lesson_cnt = options['lessons']
        courses = [generate_course_with_lessons(lesson_cnt) for _ in range(course_cnt)]

        self.stdout.write(self.style.SUCCESS(f'{len(courses)} course(s) successfully created.'))
