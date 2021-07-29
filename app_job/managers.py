from django.db import models


class ActiveJobsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_expire=False)
