from rest_framework import serializers
from apps.accounts.models import CustomUser
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
    )
    class Meta:
        model = CustomUser
        fields = ['full_name', 'phone_number', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)