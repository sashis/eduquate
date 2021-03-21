import graphene
from django.shortcuts import get_object_or_404
from graphene_django import DjangoListField, DjangoObjectType

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
        return get_object_or_404(Course, pk=id)
