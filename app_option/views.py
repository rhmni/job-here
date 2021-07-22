from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app_option import serializers
from app_option.models import Technology, City


class TechnologyListView(GenericAPIView):
    """
        show list of available technologies
    """

    serializer_class = serializers.TechnologyListSerializer

    permission_classes = (
        AllowAny,
    )

    def get(self, request):
        technologies = Technology.objects.all()
        srz_data = self.serializer_class(instance=technologies, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class CityListView(GenericAPIView):
    """
        show list of available cities
    """

    serializer_class = serializers.TechnologyListSerializer

    permission_classes = (
        AllowAny,
    )

    def get(self, request):
        cities = City.objects.all()
        srz_data = self.serializer_class(instance=cities, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)