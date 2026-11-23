
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.farmers.models import FarmerProfile
from apps.farmers.serializers import (
    FarmerProfileCreateUpdateSerializer,
    FarmerProfileSerializer,
)
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

@extend_schema(
    tags=["Farmers"],
    summary="Create farmer profile",
)
class FarmerProfileCreateView(generics.CreateAPIView):
    queryset = FarmerProfile.objects.all()
    serializer_class = FarmerProfileCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



@extend_schema(
    tags=["Farmers"],
    summary="Retrieve and update farmer profile",
)
class FarmerProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = FarmerProfileSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch", "head", "options"]

    def get_queryset(self):
        return FarmerProfile.objects.select_related(
            "user"
        ).filter(user=self.request.user)

    def get_object(self):
        return get_object_or_404(self.get_queryset())



@extend_schema(
    tags=["Farmers"],
    summary="Deactivate farmer profile",
)
class FarmerProfileDeactivateView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        farmer_profile = get_object_or_404(
            FarmerProfile,
            user=request.user,
        )

        farmer_profile.is_active = False
        farmer_profile.save(update_fields=["is_active", "updated_at"])

        return Response({
            "success": True,
            "message": "Farmer profile deactivated successfully."

        }, status=status.HTTP_200_OK)


@extend_schema(
    tags=["Farmers"],
    summary="Activate farmer profile",
)
class FarmerProfileActivateView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        farmer_profile = get_object_or_404(
            FarmerProfile,
            user=request.user,
        )

        farmer_profile.is_active = True
        farmer_profile.save(update_fields=["is_active", "updated_at"])

        return Response({
            "success": True,
            "message": "Farmer profile activated successfully."

        }, status=status.HTTP_200_OK)
