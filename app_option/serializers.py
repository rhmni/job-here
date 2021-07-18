from rest_framework import serializers

from app_option.models import Technology


class TechnologyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = (
            'id',
            'title',
            'slug',
        )
