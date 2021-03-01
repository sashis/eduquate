from django.db import models

from accounts.models import Student, Tutor


class Course(models.Model):
    name = models.CharField('название курса', max_length=100)
    description = models.TextField('описание курса')
    tutor = models.ForeignKey('accounts.Tutor', models.CASCADE, verbose_name='преподаватель')
    students = models.ManyToManyField(
        'accounts.Student',
        through='learning.CourseSubscription',
        related_name='courses',
        verbose_name='студенты'
    )

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.name


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
