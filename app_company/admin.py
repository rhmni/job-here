from django.contrib import admin

from app_company.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
