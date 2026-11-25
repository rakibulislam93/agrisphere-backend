from rest_framework import serializers
from apps.crops.models import CropVariety


class CropVarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = CropVariety
        fields = [
            'id','crop','name','name_bn','is_active',
        ]