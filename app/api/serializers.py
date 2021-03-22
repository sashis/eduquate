from rest_framework import serializers

from accounts.models import User
from courses.models import Course, Lesson


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'email',
                  'birthdate', 'gender', 'image', 'is_tutor', 'resume')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    tutor = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='user-detail'
    )
    students = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = Course
        fields = 'id', 'url', 'name', 'description', 'tutor', 'students'
