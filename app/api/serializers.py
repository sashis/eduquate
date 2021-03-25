from rest_framework import serializers

from accounts.models import User
from courses.models import Course


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'password', 'is_tutor', 'first_name',
                  'last_name', 'birthdate', 'gender', 'image', 'resume')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if plain_password := validated_data.pop('password', None):
            instance.set_password(plain_password)
        return super().update(instance, validated_data)


class AccountDetailSerializer(AccountSerializer):
    class Meta(AccountSerializer.Meta):
        fields = AccountSerializer.Meta.fields + ('courses', 'subscriptions')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = 'id', 'url', 'name', 'description', 'tutor', 'students'
        extra_kwargs = {
            'tutor': {'view_name': 'user-detail'},
            'students': {'view_name': 'user-detail'}
        }
