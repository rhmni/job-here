from django.conf import settings
from django.core.cache import cache

from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app_job.models import Job
from app_job.serializers import JobListSerializer, JobRetrieveSerializer


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


class JobRetrieveView(GenericAPIView):
    """
        get job id and show detail of job
    """

    serializer_class = JobRetrieveSerializer
    permission_classes = (
        AllowAny,
    )

    def get(self, request, job_id):
        if 'jobs' in cache:
            jobs = cache.get('jobs')
        else:
            jobs = Job.actived.all()
            cache.set('jobs', jobs, timeout=settings.JOBS_TTL_CACHE)

        job = get_object_or_404(jobs, pk=job_id)
        srz_data = self.serializer_class(instance=job)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
