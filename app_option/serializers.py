from rest_framework import serializers

from app_option.models import Technology, City


class TechnologyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = (
            'id',
            'title',
            'slug',
        )


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'title',
            'slug',
        )
