from rest_framework import serializers

from learning.models import CourseSubscription, LearningProgress


class CourseSubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        view_name='user-detail'
    )

    class Meta:
        model = CourseSubscription
        fields = 'url', 'course', 'student', 'finished'

    def create(self, validated_data):
        student = self.context['request'].user
        return CourseSubscription.objects.create(student=student, **validated_data)

    def validate_course(self, value):
        if value.tutor == self.context['request'].user:
            raise serializers.ValidationError('Нельзя подписаться на собственный курс')
        return value
