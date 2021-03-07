from eduquate.settings.helpers import insert_after, insert_before
from eduquate.settings.django import INSTALLED_APPS, MIDDLEWARE, DEBUG

if DEBUG:
    insert_after(INSTALLED_APPS, 'django.contrib.staticfiles',
                 'debug_toolbar')
    STATIC_URL = '/static/'
    insert_before(MIDDLEWARE, 'django.middleware.gzip.GZipMiddleware',
                  'debug_toolbar.middleware.DebugToolbarMiddleware')
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': 'builtins.bool'  # always true
    }