from django.contrib import admin

from app_apply.models import Apply


@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    pass
