import os

from pathlib import Path

from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('EDUQUATE_SECRET_KEY')
DEBUG = int(os.environ.get('EDUQUATE_DEBUG', default=0))
ALLOWED_HOSTS = os.environ.get('EDUQUATE_ALLOWED_HOSTS').split(' ')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'courses.apps.CoursesConfig',
    'learning.apps.LearningConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eduquate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eduquate.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('EDUQUATE_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('EDUQUATE_DB', BASE_DIR / 'db.sqlite3'),
        'USER': os.environ.get('EDUQUATE_DB_USER', 'user'),
        'PASSWORD': os.environ.get('EDUQUATE_DB_PASSWORD', 'password'),
        'HOST': os.environ.get('EDUQUATE_DB_HOST', 'localhost'),
        'PORT': os.environ.get('EDUQUATE_DB_PORT', '5432'),
    }
}

AUTH_USER_MODEL = 'accounts.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = BASE_DIR / 'static',
MEDIA_ROOT = BASE_DIR / 'images'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
LOGIN_URL = 'accounts/login'
LOGOUT_URL = 'accounts/logout'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-error'
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'
