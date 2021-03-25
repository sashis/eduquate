from django.db import models


class CourseSubscription(models.Model):
    class Meta:
        verbose_name = 'подписка на курс'
        verbose_name_plural = 'подписки на курсы'
        unique_together = ['student', 'course']

    student = models.ForeignKey(
        'accounts.Student',
        models.CASCADE,
        related_name='subscriptions',
        verbose_name='студент'
    )
    course = models.ForeignKey(
        'courses.Course',
        models.CASCADE,
        related_name='+',
        verbose_name='курс'
    )
    finished = models.BooleanField('окончен', default=False)

    def __str__(self):
        return f'{self.student} on {self.course}'


class LearningProgress(models.Model):
    class Meta:
        verbose_name = 'занятие в подписке'
        verbose_name_plural = 'занятия в подписках'
        unique_together = ['subscription', 'lesson']

    subscription = models.ForeignKey(
        CourseSubscription,
        models.CASCADE,
        related_name='progress'
    )
    lesson = models.ForeignKey(
        'courses.Lesson',
        models.CASCADE,
        related_name='+',
        verbose_name='занятие'
    )
    finished = models.BooleanField('пройдено', default=False)

    def __str__(self):
        return f'{self.lesson} for {self.subscription}'
