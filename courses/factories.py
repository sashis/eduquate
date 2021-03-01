import random

import factory

from accounts.factories import TutorFactory, fake
from .models import Course, Lesson


def generate_course_name():
    specialty = ['Разработчик', 'Тестировщик', 'Администрирование']
    names = ['C++', 'Python', 'PHP', 'Java', 'iOS-приложений',
             'Android-приложений', 'NodeJS', 'Linux', 'PostgreSQL', 'Go']
    return f'{random.choice(specialty)} {random.choice(names)}'


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.LazyFunction(generate_course_name)
    description = fake('text', max_nb_chars=500)
    tutor = factory.SubFactory(TutorFactory)


class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lesson

    seq_number = factory.Sequence(lambda n: n)
    topic = factory.Sequence(lambda n: f'Занятие {n}')
    summary = fake('text', max_nb_chars=500)
    course = factory.SubFactory(CourseFactory)


def generate_course_with_lessons(lesson_count):
    course = CourseFactory.create()
    LessonFactory.reset_sequence(1)
    LessonFactory.create_batch(lesson_count, course=course)
    return course
