from rest_framework import serializers

from accounts.models import User
from courses.models import Course


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'email',
                  'birthdate', 'gender', 'image', 'is_tutor', 'resume')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = 'id', 'url', 'name', 'description', 'tutor', 'students'
        extra_kwargs = {
            'tutor': {'view_name': 'user-detail'},
            'students': {'view_name': 'user-detail'}
        }
