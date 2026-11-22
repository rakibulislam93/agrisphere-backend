from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from apps.accounts.serializers import LoginSerializer


@extend_schema(
    tags=["Accounts"],
    summary="Login user",
)
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data)