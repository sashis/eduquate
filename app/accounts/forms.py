from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from .models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_tutor')


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm):
        model = User
        fields = ('first_name', 'last_name', 'gender', 'birthdate', 'image')
