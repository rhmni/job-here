from django.db import models

from app_company.models import Company
from app_job.managers import ActiveJobsManager, ObjectsJobManager
from app_option.models import Category, City, MinSalary, Technology


class Job(models.Model):
    MIN_EXPERIENCE = (
        ('L3', 'less than 3 year'),
        ('3T6', 'between 3 and 6 year'),
        ('G6', 'greater than 6 year'),
        ('N', 'not matter'),
    )
    JOB_TYPE = (
        ('F', 'full time'),
        ('P', 'part time'),
        ('I', 'internship'),
        ('R', 'remote'),
        ('A', 'all'),
    )
    GENDER = (
        ('M', 'male'),
        ('F', 'female'),
        ('N', 'not matter'),
    )
    MIN_DEGREE = (
        ('S', 'student'),
        ('Di', 'diploma'),
        ('B‌ٰٰٰ‌', 'bachelor'),
        ('M', 'masters'),
        ('Do', 'doctorate'),
    )
    MILITARY_STATUS = (
        ('E', 'end'),
        ('PE', 'permanent exemption'),
        ('EE', 'education exemption'),
        ('S', 'serving'),
        ('N', 'not matter'),
    )
    company = models.ForeignKey(
        to=Company,
        on_delete=models.CASCADE,
        related_name='jobs',
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='jobs',
    )
    city = models.ForeignKey(
        to=City,
        on_delete=models.CASCADE,
        related_name='jobs',
    )
    min_salary = models.ForeignKey(
        to=MinSalary,
        on_delete=models.CASCADE,
        related_name='jobs',
        help_text='blank for agreement',
        blank=True,
        null=True,
    )
    techs = models.ManyToManyField(
        to=Technology,
        related_name='jobs',
    )
    military_status = models.CharField(
        choices=MILITARY_STATUS,
        max_length=50,
    )
    title = models.CharField(max_length=150)
    min_experience = models.CharField(max_length=100, choices=MIN_EXPERIENCE)
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    gender = models.CharField(max_length=100, choices=GENDER)
    min_degree = models.CharField(max_length=100, choices=MIN_DEGREE)
    description = models.TextField()
    register_date = models.DateTimeField()
    is_expire = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    delete_date = models.DateTimeField(null=True, blank=True)

    objects = ObjectsJobManager()
    actived = ActiveJobsManager()

    def __str__(self):
        return self.title

