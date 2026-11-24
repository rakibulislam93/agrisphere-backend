from rest_framework import serializers
from apps.crops.models import Crop


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = [
            'id','name','name_bn','image','description','is_active',
            'created_at','updated_at'
        ]