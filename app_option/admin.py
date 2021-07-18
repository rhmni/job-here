from django.contrib import admin

from app_option.models import City, Technology, MinSalary, Category


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(MinSalary)
class MinSalaryAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
