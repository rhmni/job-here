from rest_framework import serializers

from app_employee.models import Employee


class RetrieveUpdateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'marital_status',
            'military_status',
            'job_status',
            'job_type',
            'title',
            'is_show_for_employers',
            'avatar',
            'about_me',
        )
