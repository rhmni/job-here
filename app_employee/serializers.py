from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app_employee.models import Employee
from app_option.models import Technology


class RetrieveUpdateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'marital_status',
            'military_status',
            'job_status',
            'job_type',
            'title',
            'is_show_for_employers',
            'avatar',
            'about_me',
            'techs_for_work',
            'cities_for_work',
            'min_salary',
            'city',
        )

class TechnologyAddDeleteSerializer(serializers.Serializer):
    techs = serializers.ListField()

    def validate_techs(self, techs):
        if not all([(type(tech) is int) for tech in techs]):
            raise ValidationError('all techs is not int')
        if len(techs) != Technology.objects.filter(pk__in=techs).count():
            raise ValidationError('some techs is not exists')
        return techs
