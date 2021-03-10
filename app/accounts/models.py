from urllib.parse import urljoin
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .managers import UserManager


def _get_unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    return f'{uuid4().hex}.{ext}'


class GenderChoice(models.TextChoices):
    MALE = 'm', 'мужской'
    FEMALE = 'f', 'женский'
    __empty__ = ''

    @property
    def image_url(self):
        image_urls = {
            'm': 'img/avatar-male.jpg',
            'f': 'img/avatar-female.jpg'
        }
        return urljoin(settings.STATIC_URL, image_urls[self.value])


class User(AbstractUser):
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
    gender = models.CharField('пол', max_length=1, choices=GenderChoice.choices, blank=True)
    image = models.ImageField('фото', upload_to=_get_unique_filename, blank=True)
    is_tutor = models.BooleanField('преподаватель', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.get_full_name() or self.email

    def get_image_url(self):
        try:
            return self.image.url
        except ValueError:
            return GenderChoice(self.gender or GenderChoice.MALE).image_url


class Student(User):
    class Meta:
        proxy = True


class Tutor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='профиль преподавателя'
    )
    resume = models.TextField('резюме', blank=True)

    class Meta:
        verbose_name_plural = 'профиль преподавателя'

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_tutor_profile(sender, instance, created, **kwargs):
    if created and instance.is_tutor:
        Tutor.objects.create(user=instance)
