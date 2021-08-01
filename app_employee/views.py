from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app_employee import serializers
from app_option.serializers import TechnologyAddDeleteSerializer
from extensions.permissions import IsEmployee


class RetrieveEmployeeView(GenericAPIView):
    """
        show profile of employee
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
        update profile of employee
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


class TechnologyAddView(GenericAPIView):
    """
        add one or more technology to employee
    """

    serializer_class = TechnologyAddDeleteSerializer
    permission_classes = (
        IsEmployee,
    )

    def patch(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            employee = request.user.employee
            techs = srz_data.validated_data['techs']
            employee.techs_for_work.add(*techs)
            return Response({'message': 'added success'}, status=status.HTTP_200_OK)


class TechnologyDeleteView(GenericAPIView):
    """
        delete one or more technology from employee
    """

    serializer_class = TechnologyAddDeleteSerializer
    permission_classes = (
        IsEmployee,
    )

    def patch(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            employee = request.user.employee
            techs = srz_data.validated_data['techs']
            employee.techs_for_work.remove(*techs)
            return Response({'message': 'deleted success'}, status=status.HTTP_200_OK)


class CityAddView(GenericAPIView):
    """
        add one or more city from employee
    """

    serializer_class = serializers.CityAddDeleteSerializer
    permission_classes = (
        IsEmployee,
    )

    def patch(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            employee = request.user.employee
            cities = srz_data.validated_data['cities']
            employee.cities_for_work.add(*cities)
            return Response({'message': 'added success'}, status=status.HTTP_200_OK)


class CityDeleteView(GenericAPIView):
    """
        delete one or more city from employee
    """

    serializer_class = serializers.CityAddDeleteSerializer
    permission_classes = (
        IsEmployee,
    )

    def patch(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            employee = request.user.employee
            cities = srz_data.validated_data['cities']
            employee.cities_for_work.remove(*cities)
            return Response({'message': 'deleted success'}, status=status.HTTP_200_OK)
