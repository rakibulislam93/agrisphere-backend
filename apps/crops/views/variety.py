from rest_framework import generics
from apps.crops.models import CropVariety
from apps.crops.serializers import CropVarietySerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from apps.farmers.permissions import IsActiveFarmer
from django.db.models import Q
from apps.common.views import FarmerBaseView


@extend_schema(
    tags=["Crops"],
    summary="List and create crop varieties",
)
class CropVarietyListCreateView(FarmerBaseView,generics.ListCreateAPIView):
    serializer_class = CropVarietySerializer
    permission_classes = [IsAuthenticated, IsActiveFarmer]

    def get_queryset(self):
        farmer = self.get_farmer()

        qs = CropVariety.objects.filter(
            Q(created_by=farmer) | 
            Q(created_by__isnull=True)
        )

        return qs.order_by('-id')

    def perform_create(self, serializer):
        serializer.save(created_by=self.get_farmer())



@extend_schema(
    tags=["Crops"],
    summary="Retrieve, update, and delete crop variety",
)
class CropVarietyDetailView(
    FarmerBaseView,
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = CropVarietySerializer
    permission_classes = [IsAuthenticated, IsActiveFarmer]

    def get_queryset(self):
        farmer = self.get_farmer()

        qs = CropVariety.objects.filter(
            Q(created_by=farmer) | 
            Q(created_by__isnull=True)
        )

        return qs.order_by('-id')
    