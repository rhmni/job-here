from datetime import datetime

from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app_job.serializers import JobListSerializer, JobRetrieveSerializer, JobCreateUpdateSerializer
from extensions.cache_queries import cache_jobs
from permissions import IsCompany


class JobListView(ListAPIView):
    """
        show list of active jobs
    """

    serializer_class = JobListSerializer
    permission_classes = (
        AllowAny,
    )

    def get_queryset(self):
        return cache_jobs()


class JobRetrieveView(GenericAPIView):
    """
        get job id and show detail of job
    """

    serializer_class = JobRetrieveSerializer
    permission_classes = (
        AllowAny,
    )

    def get(self, request, job_id):
        job = get_object_or_404(cache_jobs(), pk=job_id)
        srz_data = self.serializer_class(instance=job)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class JobCreateView(GenericAPIView):
    """
        create new job for company users
    """

    serializer_class = JobCreateUpdateSerializer
    permission_classes = (
        IsCompany,
    )

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            srz_data.save(
                company=request.user.company,
                register_date=datetime.now(),
            )
            return Response(data={'message': 'job created success'}, status=status.HTTP_200_OK)


class JobUpdateView(GenericAPIView):
    """
        create new job for company users
    """

    serializer_class = JobCreateUpdateSerializer
    permission_classes = (
        IsCompany,
    )

    def patch(self, request, job_id):
        job = get_object_or_404(cache_jobs(), pk=job_id)
        srz_data = self.serializer_class(data=request.data, instance=job, partial=True)
        if srz_data.is_valid(raise_exception=True):
            srz_data.save(
                company=request.user.company,
                register_date=datetime.now(),
            )
            return Response(data={'message': 'job updated success'}, status=status.HTTP_200_OK)
