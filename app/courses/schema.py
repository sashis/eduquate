import graphene
from graphene_django import DjangoObjectType, DjangoListField

from .models import Course, Lesson


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson


class Query(graphene.ObjectType):
    course = graphene.Field(CourseType, id=graphene.Int())
    all_courses = DjangoListField(CourseType)

    def resolve_course(root, info, id):
        return Course.objects.get(pk=id)
