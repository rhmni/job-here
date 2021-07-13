from django.conf import settings
from django.db import models


class Company(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={
            'is_active': True,
            'is_employer': True,
        }
    )
    about_us = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.name
