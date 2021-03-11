from eduquate.settings.django import INSTALLED_APPS, DEBUG

INSTALLED_APPS.append('graphene_django')

GRAPHENE = {
    'SCHEMA': 'eduquate.schema.schema'
}
if DEBUG:
    GRAPHENE['MIDDLEWARE'] = 'graphene_django.debug.DjangoDebugMiddleware'
