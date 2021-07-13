from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app_account.forms import UserChangeForm, UserCreationForm
from app_account.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone', 'id', 'name', 'is_superuser', 'is_active', 'is_employer')
    list_filter = ('is_superuser', 'is_active', 'is_employer')
    fieldsets = (
        ('Security information', {'fields': ('email', 'phone', 'password')}),
        ('Personal info', {'fields': ('name', 'age', 'gender')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_employer')}),
        ('Important date', {'fields': ('last_login', 'register_date')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'phone', 'name')
    ordering = ('-id',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
