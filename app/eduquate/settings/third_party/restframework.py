from eduquate.settings import INSTALLED_APPS

INSTALLED_APPS.append('rest_framework')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
