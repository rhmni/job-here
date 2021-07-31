from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app_apply.models import Apply
from app_employee.models import Employee
from app_option.models import Technology, City


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


class CityAddDeleteSerializer(serializers.Serializer):
    cities = serializers.ListField()

    def validate_cities(self, cities):
        if not all([(city.isnumeric()) for city in cities]):
            raise ValidationError('all cities is not int')
        if len(cities) != City.objects.filter(pk__in=cities).count():
            raise ValidationError('some cities is not exists')
        return cities


class ApplyEmployeeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = (
            'job',
            'description',
            'cv_file',
            'status',
            'register_date',
        )
