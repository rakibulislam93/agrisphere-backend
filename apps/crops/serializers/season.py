from rest_framework import serializers
from apps.crops.models import CropSeason


class CropSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropSeason
        fields = [
            'id','crop','name','name_bn','is_active',
            'created_at','updated_at'
        ]

