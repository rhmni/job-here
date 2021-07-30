from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app_option.serializers import TechnologyAddDeleteSerializer
from app_company import serializers
from permissions import IsCompany


class RetrieveCompanyView(GenericAPIView):
    """
        show profile of company
    """

    serializer_class = serializers.RetrieveUpdateCompanySerializer

    permission_classes = (
        IsCompany,
    )

    def get(self, request):
        srz_data = self.serializer_class(instance=request.user.company)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class UpdateCompanyView(GenericAPIView):
    """
        update profile of company
    """

    serializer_class = serializers.RetrieveUpdateCompanySerializer

    permission_classes = (
        IsCompany,
    )

    def patch(self, request):
        srz_data = self.serializer_class(instance=request.user.company, data=request.data, partial=True)
        if srz_data.is_valid(raise_exception=True):
            srz_data.save()
            return Response({'message': 'updated success'}, status=status.HTTP_204_NO_CONTENT)


class TechnologyAddView(GenericAPIView):
    """
        add one or more technology to company
    """

    serializer_class = TechnologyAddDeleteSerializer
    permission_classes = (
        IsCompany,
    )

    def patch(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            company = request.user.company
            techs = srz_data.validated_data['techs']
            company.technologies.add(*techs)
            return Response({'message': 'added success'}, status=status.HTTP_200_OK)


class TechnologyDeleteView(GenericAPIView):
    """
        delete one or more technology from company
    """

    serializer_class = TechnologyAddDeleteSerializer
    permission_classes = (
        IsCompany,
    )

    def patch(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            company = request.user.company
            techs = srz_data.validated_data['techs']
            company.technologies.remove(*techs)
            return Response({'message': 'deleted success'}, status=status.HTTP_200_OK)
