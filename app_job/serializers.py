from rest_framework import serializers

from app_job.models import Job


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'title',
            'company',
            'city',
            'min_salary',
            'job_type',
        )
