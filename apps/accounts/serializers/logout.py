from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from apps.common.exceptions import UnauthorizedException
from rest_framework_simplejwt.exceptions import TokenError



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(write_only=True)

    def validate(self, attrs):
        try:
            token = RefreshToken(attrs['refresh'])
            request_user = self.context['request'].user

            if str(token.get('user_id')) != str(request_user.id):
                raise UnauthorizedException(
                    message="Invalid refresh token."
                )
            self.token = token

        except TokenError:
            raise UnauthorizedException(
                message="Invalid or expired refresh token."
            )

        return attrs

    def save(self, **kwargs):
        self.token.blacklist()