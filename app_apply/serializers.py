from rest_framework import serializers

from app_apply.models import Apply
from app_employee.models import Employee
from app_job.models import Job


class JobNestedSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'title',
        )


class EmployeeNestedSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'marital_status',
            'military_status',
            'job_status',
            'job_type',
            'title',
            'avatar',
            'about_me',
            'techs_for_work',
            'cities_for_work',
            'min_salary',
            'city',
        )


class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = (
            'employee',
            'job',
            'description',
            'cv_file',
            'status',
            'register_date',
        )

        read_only_fields = (
            'employee',
            'job',
            'status',
            'register_date',
        )


class ApplyListForEmployeeSerializer(serializers.ModelSerializer):
    job = JobNestedSerialiser()

    class Meta:
        model = Apply
        fields = (
            'pk',
            'job',
            'status',
            'register_date',
        )


class ApplyRetrieveForEmployeeSerializer(serializers.ModelSerializer):
    employee = EmployeeNestedSerialiser(read_only=True)

    class Meta:
        model = Apply
        fields = (
            'employee',
            'description',
            'cv_file',
            'status',
            'register_date',
        )


class ApplyListForCompanySerializer(serializers.ModelSerializer):
    job = JobNestedSerialiser()

    class Meta:
        model = Apply
        fields = (
            'pk',
            'employee',
            'status',
            'register_date',
        )
