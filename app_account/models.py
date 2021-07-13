from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.db import models
from .managers import UserManager


def phone_validate(value):
    if len(value) != 11:
        raise ValidationError('phone must be 11 character')
    if not value.isnumeric():
        raise ValidationError('phone must be only number')
    if not value.startswith('09'):
        raise ValidationError('phone must start with "09"')


class User(AbstractBaseUser):
    GENDER = (
        ('M', 'male'),
        ('F', 'female'),
    )
    email = models.EmailField(max_length=200, unique=True, null=True, blank=True)
    gender = models.CharField(null=True, blank=True, choices=GENDER, max_length=50)
    phone = models.CharField(max_length=20, unique=True, validators=[phone_validate], null=True, blank=True)
    name = models.CharField(max_length=150)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    join_date = models.DateTimeField(null=True, blank=True)
    is_employer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser
