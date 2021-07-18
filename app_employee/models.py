from django.conf import settings
from django.db import models

from app_option.models import Technology, MinSalary, City


class Employee(models.Model):
    JOB_STATUS = (
        ('E', 'employed'),
        ('JS', 'job seeker'),
        ('LFBJ', 'looking for better job'),
    )
    JOB_TYPE = (
        ('F', 'full time'),
        ('P', 'part time'),
        ('I', 'internship'),
        ('R', 'remote'),
    )
    MARITAL_STATUS = (
        ('M', 'married'),
        ('S', 'single'),
    )
    MILITARY_STATUS = (
        ('I', 'included'),
        ('E', 'end'),
        ('PE', 'permanent exemption'),
        ('EE', 'education exemption'),
        ('S', 'serving'),
    )
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={
            'is_active': True,
            'is_company': False,
        }
    )
    marital_status = models.CharField(
        null=True,
        blank=True,
        choices=MARITAL_STATUS,
        max_length=50,
    )
    military_status = models.CharField(
        null=True,
        blank=True,
        choices=MILITARY_STATUS,
        max_length=50,
    )
    job_status = models.CharField(
        null=True,
        blank=True,
        choices=JOB_STATUS,
        max_length=70,
    )
    job_type = models.CharField(
        null=True,
        blank=True,
        choices=JOB_TYPE,
        max_length=70,
    )
    title = models.CharField(max_length=200, null=True, blank=True)
    is_show_for_employers = models.BooleanField(default=True)
    avatar = models.ImageField(default='default_employee_avatar.jpg')
    about_me = models.TextField(null=True, blank=True)

    techs_for_work = models.ManyToManyField(
        to=Technology,
        related_name='employees',
        blank=True,
    )
    cities_for_work = models.ManyToManyField(
        to=City,
        related_name='employees_for_work',
        blank=True,
    )

    min_salary = models.ForeignKey(
        to=MinSalary,
        on_delete=models.SET_NULL,
        related_name='employees',
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        to=City,
        on_delete=models.SET_NULL,
        related_name='employees',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.name
