from django.contrib.messages import constants as messages

from .django import INSTALLED_APPS, DATABASES
from .helpers import env, BASE_DIR

INSTALLED_APPS.extend([
    'accounts.apps.AccountsConfig',
    'courses.apps.CoursesConfig',
    'learning.apps.LearningConfig',
    'contacts.apps.ContactsConfig',
    'api.apps.ApiConfig',
])

if db_params := env.db('DATABASE_URL'):
    DATABASES.update({'default': db_params})

AUTH_USER_MODEL = 'accounts.User'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

LOGIN_URL = '/accounts/login'
LOGOUT_URL = '/accounts/logout'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-error'
}

ADMINS = [
    ('Site Admin', 'admin@eduquate.com')
]
DEFAULT_FROM_EMAIL = 'no-reply@eduquate.com'
EMAIL_SUBJECT_PREFIX = '[EduQuate Site Message] '
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
