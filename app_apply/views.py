from datetime import datetime

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404, ListAPIView
from rest_framework.response import Response

from extensions.paginations import StandardPagination
from extensions.permissions import IsEmployee, IsOwnerOfApplyEmployee, IsOwnerOfJob
from app_apply.models import Apply
from app_job.models import Job
from app_apply.serializers import (
    ApplyJobSerializer,
    ApplyListForEmployeeSerializer,
    ApplyRetrieveForEmployeeSerializer,
)


class ApplyJobView(GenericAPIView):
    """
        apply for job by employee user
    """
    serializer_class = ApplyJobSerializer
    permission_classes = (
        IsEmployee,
    )

    def post(self, request, job_id):
        job = get_object_or_404(Job.actived, pk=job_id)
        if Apply.objects.filter(job=job, employee=request.user.employee).exists():
            return Response(data={'message': 'you already apply for this job'}, status=status.HTTP_400_BAD_REQUEST)
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            srz_data.save(
                employee=request.user.employee,
                job=job,
                status='N',
                register_date=datetime.now(),
            )
            return Response(data={'message': 'apply success'}, status=status.HTTP_200_OK)


class ApplyListForEmployeeView(ListAPIView):
    """
        return all apply of employee user
    """

    serializer_class = ApplyListForEmployeeSerializer
    pagination_class = StandardPagination
    permission_classes = (
        IsEmployee,
    )

    def get_queryset(self):
        return Apply.objects.filter(employee=self.request.user.employee)


class ApplyRetrieveForEmployeeView(GenericAPIView):
    """
        get apply_id and return detail of it for owner employee
    """

    serializer_class = ApplyRetrieveForEmployeeSerializer
    permission_classes = (
        IsOwnerOfApplyEmployee,
    )

    def get(self, request, apply_id):
        apply = get_object_or_404(Apply, pk=apply_id)
        self.check_object_permissions(request, apply)
        srz_data = self.serializer_class(instance=apply)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class ApplyListForCompanyView(ListAPIView):
    """
        get job_id and return all applys for owner company
    """

    serializer_class = ApplyListForEmployeeSerializer
    pagination_class = StandardPagination
    permission_classes = (
        IsOwnerOfJob,
    )

    def get_queryset(self):
        job = get_object_or_404(Job.objects, pk=self.kwargs['job_id'])
        self.check_object_permissions(self.request, job)
        applys = Apply.objects.filter(job=job)
        return applys


class ApplyRetrieveForCompanyView(GenericAPIView):
    """
        get apply_id and return detail of it for owner company
    """

    serializer_class = ApplyRetrieveForEmployeeSerializer
    permission_classes = (
        IsOwnerOfApplyEmployee,
    )

    def get(self, request, apply_id):
        apply = get_object_or_404(Apply.objects, pk=apply_id)
        self.check_object_permissions(request, apply)
        srz_data = self.serializer_class(instance=apply)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
