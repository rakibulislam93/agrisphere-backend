from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from apps.common.exceptions import (
    UnauthorizedException,
    ForbiddenException,
)


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            phone_number=attrs.get("phone_number"),
            password=attrs.get("password"),
        )
        if not user:
            raise UnauthorizedException(
                message="Invalid phone number or password."
            )
        if not user.is_active:
            raise ForbiddenException(
                message="This account is inactive. Please contact support."
            )

        refresh = RefreshToken.for_user(user)

        return {
            "user": {
                "id": user.id,
                "phone_number": user.phone_number,
                "full_name": user.full_name,
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }