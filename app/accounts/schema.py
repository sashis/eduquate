import graphene
from graphene_django import DjangoListField
from graphene_django.types import DjangoObjectType

from .models import User, Student, Tutor


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = 'password',

    full_name = graphene.String()

    def resolve_full_name(parent, info):
        return parent.get_full_name()


class StudentType(UserType):
    class Meta:
        model = Student
        exclude = 'password',


class TutorType(DjangoObjectType):
    class Meta:
        model = Tutor


class Query(graphene.ObjectType):
    student = graphene.Field(StudentType, id=graphene.Int())
    all_students = DjangoListField(StudentType)

    def resolve_student(root, info, id):
        return Student.objects.get(pk=id)
