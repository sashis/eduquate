import graphene
from django.shortcuts import get_object_or_404
from graphene_django import DjangoListField
from graphene_django.types import DjangoObjectType

from .models import Student, Tutor, User
from courses.schema import CourseType


class UserType(DjangoObjectType):
    class Meta:
        model = User

    full_name = graphene.String()

    def resolve_full_name(parent, info):
        return parent.get_full_name()


class StudentType(UserType):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'email', 'birthdate',
                  'gender', 'image', 'resume', 'subscribed_courses')


class TutorType(UserType):

    courses = DjangoListField(CourseType)

    class Meta:
        model = Tutor
        fields = ('id', 'first_name', 'last_name', 'email', 'birthdate',
                  'gender', 'image', 'resume')


class Query(graphene.ObjectType):
    student = graphene.Field(StudentType, id=graphene.Int())
    tutor = graphene.Field(TutorType, id=graphene.Int())
    all_students = DjangoListField(StudentType)
    all_tutors = DjangoListField(TutorType)

    def resolve_student(root, info, id):
        return get_object_or_404(Student, pk=id)

    def resolve_tutor(root, info, id):
        return get_object_or_404(Tutor, pk=id)
