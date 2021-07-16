from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app_account.models import User


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=150)
    password = serializers.CharField()
    is_company = serializers.BooleanField(default=False)

    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError('password is short')

        if not any([char.isnumeric() for char in password]):
            raise ValidationError('number is not in your password')

        if not any([char.isupper() for char in password]):
            raise ValidationError('upper char is not in your password')

        if not any([char.islower() for char in password]):
            raise ValidationError('lower char is not in your password')

        if not any([symbol in password for symbol in '"!@#$%^&*()_-+={}[]\|/']):
            raise ValidationError('symbol is not in your password')

        return password

    def validate_email(self, email):
        user = User.objects.filter(email=email)
        if user.exists() and user[0].is_active:
            raise ValidationError('this field must be unique')
        return email


class UserChangeEmailSerializer(serializers.Serializer):
    new_email = serializers.EmailField()
    password = serializers.CharField()

    def validate_new_email(self, email):
        user = User.objects.filter(email=email)
        if user.exists() and user[0].is_active:
            raise ValidationError('this field must be unique')
        return email
