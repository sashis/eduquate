from django.db import models
from django.db.models.functions import Coalesce
from django.urls import reverse


class CourseManager(models.Manager):
    def with_rating(self, ordered=False):
        rated_courses = self.annotate(
            rating=Coalesce(models.Count('students'), 0))
        return rated_courses.order_by('-rating') if ordered else rated_courses


class Course(models.Model):
    name = models.CharField('название курса', max_length=100)
    description = models.TextField('описание курса')
    tutor = models.ForeignKey(
        'accounts.Tutor',
        models.CASCADE,
        related_name='courses',
        verbose_name='преподаватель'
    )
    students = models.ManyToManyField(
        'accounts.Student',
        through='learning.CourseSubscription',
        related_name='subscribed_courses',
        verbose_name='студенты'
    )

    objects = CourseManager()

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:detail', args=[self.pk])


class Lesson(models.Model):
    seq_number = models.PositiveSmallIntegerField('порядковый номер занятия', null=False, default=1)
    topic = models.CharField('тема занятия', max_length=100)
    summary = models.TextField('содержание занятия', blank=True)
    course = models.ForeignKey(Course, models.CASCADE,
                               related_name='lessons', verbose_name='курс')

    class Meta:
        verbose_name = 'занятие'
        verbose_name_plural = 'занятия'
        ordering = ['seq_number']

    def __str__(self):
        return self.topic
