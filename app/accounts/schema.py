import graphene

from graphene_django.types import DjangoObjectType, ObjectType

from .models import Student, Tutor


class StudentType(DjangoObjectType):
    """Student model"""
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name', 'gender', 'image')

    gender = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, info):
        return self.get_full_name()

    def resolve_gender(self, info):
        return self.get_gender_display()
    

class Query(ObjectType):
    student = graphene.Field(StudentType, id=graphene.Int())
    all_students = graphene.List(StudentType)

    def resolve_student(self, info, **kwargs):
        id = kwargs.get('id')
        return Student.objects.get(pk=id)

    def resolve_all_students(self, info, **kwargs):
        return Student.objects.all()
