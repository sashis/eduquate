import factory
from django.conf import settings

from .models import User, Student, Tutor


def fake(provider, **kwargs):
    return factory.Faker(provider, locale=settings.LANGUAGE_CODE, **kwargs)


class PersonFactory(factory.StubFactory):
    class Params:
        male = factory.Trait(
            gender=User.Gender.MALE,
            first_name=fake('first_name_male'),
            last_name=fake('last_name_male')
        )

    gender = User.Gender.FEMALE
    first_name = fake('first_name_female')
    last_name = fake('last_name_female')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        exclude = 'person', 'is_male', 'plain_password'

    plain_password = 'defaultpassword'
    is_male = fake('pybool')
    person = factory.SubFactory(PersonFactory, male=factory.SelfAttribute('..is_male'))
    email = fake('email')
    password = factory.PostGenerationMethodCall('set_password', plain_password)
    gender = factory.SelfAttribute('person.gender')
    first_name = factory.SelfAttribute('person.first_name')
    last_name = factory.SelfAttribute('person.last_name')
    birthdate = fake('date_between', start_date='-45y', end_date='-18y')


class StudentFactory(UserFactory):
    class Meta:
        model = Student

    is_tutor = False


class TutorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tutor

    user = factory.SubFactory(UserFactory, is_tutor=True)
    resume = fake('text', max_nb_chars=1000)
