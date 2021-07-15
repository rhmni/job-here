from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app_employee import serializers
from permissions import IsEmployee


class RetrieveEmployeeView(GenericAPIView):
    """
        show data of employee for himself
    """

    serializer_class = serializers.RetrieveUpdateEmployeeSerializer

    permission_classes = (
        IsEmployee,
    )

    def get(self, request):
        srz_data = self.serializer_class(instance=request.user.employee)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class UpdateEmployeeView(GenericAPIView):
    """
        update employee data
    """

    serializer_class = serializers.RetrieveUpdateEmployeeSerializer

    permission_classes = (
        IsEmployee,
    )

    def patch(self, request):
        srz_data = self.serializer_class(instance=request.user.employee, data=request.data, partial=True)
        if srz_data.is_valid(raise_exception=True):
            srz_data.save()
            return Response({'message': 'updated success'}, status=status.HTTP_204_NO_CONTENT)


