from rest_framework import serializers

from app_company.models import Company


class CompanyRetrieveUpdateSerializer(serializers.ModelSerializer):
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



