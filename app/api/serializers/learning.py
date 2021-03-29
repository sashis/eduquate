from rest_framework import serializers

from learning.models import CourseSubscription, LearningProgress


class CourseSubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = 'id', 'url', 'course', 'student', 'finished', 'progress'
        extra_kwargs = {
            'student': {'view_name': 'user-detail'}
        }


class LearningProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningProgress
        fields = 'lesson', 'finished'
