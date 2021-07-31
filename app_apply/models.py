from django.db import models

from app_employee.models import Employee
from app_job.models import Job
from app_option.tasks import send_email


class Apply(models.Model):
    STATUS = (
        ('CFI', 'confirmation for interview'),
        ('F', 'failed'),
        ('H', 'hired'),
        ('S', 'see'),
        ('N', 'not see'),
    )
    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE,
        related_name='applys',
    )
    job = models.ForeignKey(
        to=Job,
        on_delete=models.CASCADE,
        related_name='applys',
    )
    description = models.TextField(null=True, blank=True)
    cv_file = models.FileField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default='N')
    register_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.job.title

    class Meta:
        unique_together = ('job', 'employee')

    def save(self, *args, **kwargs):
        if not self.pk:
            send_email.delay(
                subject='درخواست شما ارسال شد',
                message=f' درخواست شما برای {self.job.title} ارسال شد ',
                email=self.employee.user.email,
            )
        if self.pk:
            send_email.delay(
                subject='وضعیت درخواست شما تغییر کرد',
                message=f' وضعیت درخواست شما برای موقعیت {self.job.title} به {self.status} تغییر کرد ',
                email=self.employee.user.email,
            )
        super().save(*args, **kwargs)
