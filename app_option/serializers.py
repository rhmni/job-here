from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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


class TechnologyAddDeleteSerializer(serializers.Serializer):
    techs = serializers.ListField()

    def validate_techs(self, techs):
        if not all([(tech.isnumeric()) for tech in techs]):
            raise ValidationError('all techs is not int')
        if len(techs) != Technology.objects.filter(pk__in=techs).count():
            raise ValidationError('some techs is not exists')
        return techs
