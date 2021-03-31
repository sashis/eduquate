from rest_framework import serializers

from courses.models import Course
from ..serializers import AccountListSerializer


class CourseListSerializer(serializers.HyperlinkedModelSerializer):
    num_students = serializers.IntegerField(read_only=True)
    num_lessons = serializers.IntegerField(read_only=True)
    tutor = AccountListSerializer(read_only=True)

    class Meta:
        model = Course
        fields = 'url', 'name', 'tutor', 'num_lessons', 'num_students'


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = 'url', 'name', 'description', 'tutor', 'students'
        read_only_fields = 'tutor', 'students'
        extra_kwargs = {
            'tutor': {'view_name': 'user-detail'},
            'students': {'view_name': 'user-detail'}
        }

    def create(self, validated_data):
        tutor = self.context['request'].user
        return Course.objects.create(tutor=tutor, **validated_data)