from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = self.instance

        if not user.check_password(attrs["current_password"]):
            raise ValidationError({
                "current_password": "Current password is incorrect."
            })

        if attrs["new_password"] != attrs["confirm_password"]:
            raise ValidationError({
                "confirm_password": "Passwords do not match."
            })

        if attrs["current_password"] == attrs["new_password"]:
            raise ValidationError({
                "new_password": "New password must be different."
            })

        validate_password(attrs["new_password"], user=user)

        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()

        # Blacklist all existing refresh tokens of this user.
        outstanding_tokens = OutstandingToken.objects.filter(
            user=instance
        )

        for token in outstanding_tokens:
            BlacklistedToken.objects.get_or_create(token=token)

        return instance