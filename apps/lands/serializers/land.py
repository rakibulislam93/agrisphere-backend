from rest_framework import serializers
from apps.lands.models import Land



class LandCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = [
            'id','name','area','land_type','location','is_active'
        ]

    def validate_area(self, value):
        if value <= 0:
            raise serializers.ValidationError("Area must be a positive number.")
        return value



class LandSerializer(serializers.ModelSerializer):
    farmer_name = serializers.CharField(
        source='farmer.user.full_name',
        read_only=True
    )
    farmer_phone_number = serializers.CharField(
        source='farmer.user.phone_number',
        read_only=True
    )

    class Meta:
        model = Land
        fields = [
            'id','farmer','farmer_name','farmer_phone_number','name','area',
            'land_type','location','is_active','created_at','updated_at'
        ]