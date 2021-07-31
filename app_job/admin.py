from django.contrib import admin

from app_job.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pk',
    )
