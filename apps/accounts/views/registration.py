from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from apps.accounts.serializers import RegistrationSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=["Accounts"],
    summary="Register a new user",
)
class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]