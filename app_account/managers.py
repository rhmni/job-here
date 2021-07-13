from django.contrib.auth.base_user import BaseUserManager

from app_account import models


class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not name:
            raise ValueError('Users must have an name')
        if not email:
            raise ValueError('Users must have a email')

        user = self.model(
            name=name,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):

        user = self.create_user(
            name=name,
            password=password,
            email=email,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_or_create(self, name, email, password=None):
        try:
            user = models.User.objects.get(email=email)
            created = False
        except models.User.DoesNotExist:
            user = self.create_user(
                name=name,
                password=password,
                email=email,
            )
            created = True
        return user, created
