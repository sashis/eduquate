from rest_framework import serializers

from courses.models import Course, Lesson
from ..serializers import AccountTerseSerializer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    num_students = serializers.IntegerField(read_only=True)
    num_lessons = serializers.IntegerField(read_only=True)
    tutor = AccountTerseSerializer(read_only=True)

    class Meta:
        model = Course
        fields = 'id', 'url', 'name', 'description', 'tutor', 'num_lessons', 'num_students'


class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
    students = AccountTerseSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = 'id', 'url', 'name', 'description', 'tutor', 'lessons', 'students'
