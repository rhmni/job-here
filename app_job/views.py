from datetime import datetime

from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from extensions.filters import JobFilter
from extensions.paginations import StandardPagination, SmalPagination
from extensions.permissions import IsCompany, IsOwnerOfJob, IsEmployee
from app_job.models import Job
from app_job.serializers import (
    JobListSerializer,
    JobRetrieveSerializer,
    JobCreateUpdateSerializer,
    JobRetrieveForCompanySerializer,
)


class JobListView(ListAPIView):
    """
        return list of active jobs for all users
    """

    serializer_class = JobListSerializer
    pagination_class = StandardPagination
    filterset_class = JobFilter
    filter_backends = (
        filters.DjangoFilterBackend,
    )
    permission_classes = (
        AllowAny,
    )

    def get_queryset(self):
        return Job.actived.all()


class JobRetrieveView(GenericAPIView):
    """
        get job_id and show detail of job for all users
    """

    serializer_class = JobRetrieveSerializer
    permission_classes = (
        AllowAny,
    )

    def get(self, request, job_id):
        job = get_object_or_404(Job.actived, pk=job_id)
        srz_data = self.serializer_class(instance=job)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class JobCreateForCompanyView(GenericAPIView):
    """
        create new job for company
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


class JobUpdateForCompanyView(GenericAPIView):
    """
        get job_id and update job by owner of company
    """

    serializer_class = JobCreateUpdateSerializer
    permission_classes = (
        IsOwnerOfJob,
    )

    def patch(self, request, job_id):
        job = get_object_or_404(Job.actived, pk=job_id)
        self.check_object_permissions(request, job)
        srz_data = self.serializer_class(data=request.data, instance=job, partial=True)
        if srz_data.is_valid(raise_exception=True):
            srz_data.save(
                company=request.user.company,
                register_date=datetime.now(),
            )
            return Response(data={'message': 'job updated success'}, status=status.HTTP_200_OK)


class JobDeleteForCompanyView(GenericAPIView):
    """
        get job_id and delete job by owner of company
    """

    permission_classes = (
        IsOwnerOfJob,
    )

    def delete(self, request, job_id):
        job = get_object_or_404(Job.objects, pk=job_id)
        self.check_object_permissions(request, job)
        job.is_delete = True
        job.delete_date = datetime.now()
        job.save()
        return Response(data={'message': 'job deleted success'}, status=status.HTTP_200_OK)


class JobListForCompanyView(ListAPIView):
    """
        return list of jobs for company
    """

    serializer_class = JobListSerializer
    pagination_class = StandardPagination
    permission_classes = (
        IsCompany,
    )

    def get_queryset(self):
        return Job.objects.filter(company=self.request.user.company)


class JobRetrieveForCompanyView(GenericAPIView):
    """
        get job_id and return detail of job for company
    """

    serializer_class = JobRetrieveForCompanySerializer
    permission_classes = (
        IsOwnerOfJob,
    )

    def get(self, request, job_id):
        job = get_object_or_404(Job.objects, pk=job_id)
        self.check_object_permissions(request, job)
        srz_data = self.serializer_class(instance=job)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class SimilarJobsView(GenericAPIView):
    """
        get job_id and return list of 5 similar jobs
    """

    serializer_class = JobListSerializer
    permission_classes = (
        AllowAny,
    )

    def get(self, request, job_id):
        job = get_object_or_404(Job.actived, pk=job_id)
        tech_ids = job.techs.values_list('pk', flat=True)
        jobs = Job.actived.filter(techs__pk__in=tech_ids).exclude(pk=job.pk)[:5]
        srz_data = self.serializer_class(instance=jobs, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class RecommendJobsView(ListAPIView):
    """
        return list of recommend jobs for employee
    """

    serializer_class = JobListSerializer
    pagination_class = SmalPagination
    permission_classes = (
        IsEmployee,
    )

    def get_queryset(self):
        tech_ids = self.request.user.employee.techs_for_work.values_list('pk', flat=True)
        return Job.actived.filter(techs__pk__in=tech_ids)
