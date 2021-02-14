from django.db import models

from accounts.models import Student, Tutor


class Course(models.Model):
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    name = models.CharField('название курса', max_length=100)
    description = models.TextField('описание курса')
    tutor = models.ForeignKey(Tutor, models.CASCADE, verbose_name='преподаватель')
    students = models.ManyToManyField(Student, through='Learning', verbose_name='студенты')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    class Meta:
        verbose_name = 'занятие'
        verbose_name_plural = 'занятия'

    topic = models.CharField('тема занятия', max_length=100)
    summary = models.TextField('содержание занятия', blank=True)
    course = models.ForeignKey(Course, models.CASCADE, verbose_name='курс')

    def __str__(self):
        return self.topic


class Learning(models.Model):
    student = models.ForeignKey(Student, models.CASCADE)
    course = models.ForeignKey(Course, models.CASCADE)

    def __str__(self):
        return f'{self.student.get_full_name()} on {self.course.name}'
