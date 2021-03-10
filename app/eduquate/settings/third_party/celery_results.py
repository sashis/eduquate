from eduquate.settings.helpers import env
from eduquate.settings.django import INSTALLED_APPS

INSTALLED_APPS.append('django_celery_results')

CELERY_BROKER_URL = env('BROKER_URL')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
