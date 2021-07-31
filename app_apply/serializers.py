from rest_framework import serializers

from app_apply.models import Apply


class ApplyForJobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = (
            'employee',
            'job',
            'description',
            'cv_file',
            'status',
            'register_date',
        )

        read_only_fields = (
            'employee',
            'job',
            'status',
            'register_date',
        )
