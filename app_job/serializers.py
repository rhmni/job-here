from rest_framework import serializers

from app_job.models import Job
from app_option.models import Technology


class TechnologyNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = (
            'title',
        )


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'pk',
            'title',
            'company',
            'city',
            'min_salary',
            'job_type',
        )


class JobRetrieveSerializer(serializers.ModelSerializer):
    techs = TechnologyNestedSerializer(many=True)

    class Meta:
        model = Job
        fields = (
            'title',
            'company',
            'city',
            'min_salary',
            'job_type',
            'category',
            'techs',
            'military_status',
            'min_experience',
            'gender',
            'min_degree',
            'description',
            'register_date',
        )


class JobCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'title',
            'company',
            'city',
            'min_salary',
            'job_type',
            'category',
            'techs',
            'military_status',
            'min_experience',
            'gender',
            'min_degree',
            'description',
            'register_date',
        )

        read_only_fields = (
            'register_date',
            'company',
        )


class JobRetrieveForCompanySerializer(serializers.ModelSerializer):
    techs = TechnologyNestedSerializer(many=True)

    class Meta:
        model = Job
        fields = (
            'pk',
            'title',
            'city',
            'min_salary',
            'job_type',
            'category',
            'techs',
            'military_status',
            'min_experience',
            'gender',
            'min_degree',
            'description',
            'register_date',
            'is_expire',
        )
