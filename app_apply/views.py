from datetime import datetime

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from app_apply.models import Apply
from app_apply.serializers import ApplyForJobSerializers
from app_job.models import Job
from permissions import IsEmployee


class ApplyForJobView(GenericAPIView):
    """
        apply for job by employee user
    """
    serializer_class = ApplyForJobSerializers
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
