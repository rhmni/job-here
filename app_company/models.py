from django.conf import settings
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    NUMBER_OF_EMPLOYEES = (
        ('1T10', '1 to 10'),
        ('10T50', '10 to 50'),
        ('50T100', '50 to 100'),
        ('100T250', '100 to 250'),
        ('250T1000', '250 to 1000'),
        ('+1000', 'more than thousand'),
    )
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={
            'is_active': True,
            'is_employer': True,
        }
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        related_name='companies',
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    logo = models.ImageField(default='default_company_logo.jpg')
    web_site = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    email = models.URLField(null=True, blank=True)
    number_of_employees = models.CharField(max_length=150, choices=NUMBER_OF_EMPLOYEES, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    about_us = models.TextField(null=True, blank=True)

    # todo : techs

    def __str__(self):
        return self.user.name
