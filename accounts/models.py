from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


def _get_unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    return f'{uuid4().hex}.{ext}'


class User(AbstractUser):

    class Gender(models.TextChoices):
        MALE = 'm', 'мужской'
        FEMALE = 'f', 'женский'
        __empty__ = ''

    username = None
    # is_staff = None
    email = models.EmailField(
        'адрес электронной почты',
        unique=True,
        blank=False,
        error_messages={
            'unique': 'пользователь с таким e-mail уже зарегистрирован',
            'blank': 'необходимо задать e-mail',
        }
    )
    birthdate = models.DateField('дата рождения', blank=True, null=True)
    gender = models.CharField('пол', max_length=1, choices=Gender.choices, blank=True)
    image = models.ImageField('фото', upload_to=_get_unique_filename, blank=True)
    is_tutor = models.BooleanField('преподаватель', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_tutor']
    objects = UserManager()

    def save(self, *args, **kwargs):
        tutor_created = self.pk is None and self.is_tutor
        super().save(*args, **kwargs)
        if tutor_created:
            Tutor.objects.create(user=self)
            self.tutor.save()


class Student(User):
    class Meta:
        proxy = True


class Tutor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        parent_link=True
    )
    resume = models.TextField('резюме', blank=True)
