from rest_framework import serializers

from app_apply.models import Apply
from app_job.models import Job


class JobNestedSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'title',
        )


class ApplyForJobSerializer(serializers.ModelSerializer):
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


class ApplyListSerializer(serializers.ModelSerializer):
    job = JobNestedSerialiser()

    class Meta:
        model = Apply
        fields = (
            'pk',
            'job',
            'status',
            'register_date',
        )
