from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.get_full_name() or self.email


class Student(User):
    class Meta:
        proxy = True


class Tutor(models.Model):
    class Meta:
        verbose_name_plural = 'профиль преподавателя'

    # pk = 'user_id'
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='профиль преподавателя'
    )
    resume = models.TextField('резюме', blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_tutor_profile(sender, instance, created, **kwargs):
    if created and instance.is_tutor:
        Tutor.objects.create(user=instance)
