from django.conf import settings
from django.core.cache import cache

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from app_job.models import Job
from app_job.serializers import JobListSerializer


class JobListView(ListAPIView):
    """
        show list of active jobs
    """

    serializer_class = JobListSerializer
    permission_classes = (
        AllowAny,
    )

    def get_queryset(self):
        if 'jobs' in cache:
            jobs = cache.get('jobs')
        else:
            jobs = Job.actived.all()
            cache.set('jobs', jobs, timeout=settings.JOBS_TTL_CACHE)

        return jobs

