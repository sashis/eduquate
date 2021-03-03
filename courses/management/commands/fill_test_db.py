from random import choices

from django.core.management import BaseCommand

from accounts.factories import StudentFactory, TutorFactory
from courses.factories import generate_course_with_lessons


class Command(BaseCommand):
    help = (
        'Fill DB with 10 courses by 10 tutors. Each course consist of 10 lessons. '
        'Each of 10 students are randomly subscribed for 5 courses.'
    )

    def handle(self, *args, **kwargs):
        courses_count = 10
        lessons_count = 10
        students_count = 10
        subscription_count = 5

        courses = [generate_course_with_lessons(lessons_count) for _ in range(courses_count)]
        students = [StudentFactory() for _ in range(students_count)]

        for student in students:
            courses_to_subscribe = choices(courses, k=subscription_count)
            student.subscribed_courses.add(*courses_to_subscribe)

        self.stdout.write(self.style.SUCCESS('DB filled with test data successfully.'))
