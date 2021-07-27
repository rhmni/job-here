from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app_company.models import Company
from app_option.models import Technology


class RetrieveUpdateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'category',
            'title',
            'slug',
            'logo',
            'web_site',
            'linkedin',
            'email',
            'number_of_employees',
            'address',
            'about_us',
        )



