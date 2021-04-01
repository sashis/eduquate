from eduquate.settings.django import INSTALLED_APPS, MIDDLEWARE, DEBUG
from eduquate.settings.helpers import insert_before

INSTALLED_APPS.append('corsheaders')

insert_before(MIDDLEWARE, 'django.middleware.common.CommonMiddleware',
              'corsheaders.middleware.CorsMiddleware')

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://localhost:3000'
]
