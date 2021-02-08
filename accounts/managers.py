from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **other_fields):
        user = self.model(email=self.normalize_email(email), **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **other_fields):
        other_fields.update({
            'is_staff': False,
            'is_superuser': False,
        })
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password, **other_fields):
        other_fields.update({
            'is_staff': True,
            'is_superuser': True,
        })
        return self._create_user(email, password, **other_fields)