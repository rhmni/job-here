from django.db import models


class ActiveJobsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False, is_expire=False)


class ObjectsJobManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)
