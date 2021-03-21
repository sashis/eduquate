from rest_framework import serializers

from accounts.models import User


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'email',
                  'birthdate', 'gender', 'image', 'is_tutor', 'resume')
