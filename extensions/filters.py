from django_filters import rest_framework as filters

from app_job.models import Job


class JobFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    des = filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = (
            'gender',
            'category',
            'city',
            'min_salary',
            'techs',
            'title',
            'des',
            'military_status',
            'min_experience',
            'job_type',
            'min_degree',
        )
