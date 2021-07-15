from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app_company import serializers
from permissions import IsCompany


class RetrieveCompanyView(GenericAPIView):
    """
        show data of company for founder
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
        update company data
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
