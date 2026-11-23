from rest_framework import serializers
from apps.farmers.models import FarmerProfile


class FarmerProfileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProfile
        fields = [
            'profile_image','date_of_birth','gender','religion','marital_status',
            'division','district','upazila','union','village'
        ]

    def validate(self, attrs):
        user = self.context['request'].user
        
        if FarmerProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError("Farmer profile already exists for this user.")
        return attrs

class FarmerProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name', read_only=True)
    phone_number = serializers.CharField(source='user.phone_number', read_only=True)

    class Meta:
        model = FarmerProfile
        fields = [
            'id','user','full_name','phone_number','profile_image','date_of_birth','gender',
            'religion','marital_status','division','district','upazila','union','village',
            'is_active','created_at','updated_at'
        ]