from django.conf import settings
from graphene import Field, Schema, ObjectType
from graphene_django.debug import DjangoDebug

from accounts.schema import Query as AccountQuery
from courses.schema import Query as CourseQuery


class Query(AccountQuery, CourseQuery, ObjectType):
    debug = Field(DjangoDebug, name='_debug') if settings.DEBUG else None


schema = Schema(query=Query)
