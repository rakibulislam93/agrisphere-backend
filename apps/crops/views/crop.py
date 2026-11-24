from rest_framework import generics
from apps.crops.models import Crop
from apps.crops.serializers import CropSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAdminUser

@extend_schema(
    tags=["Crops"],
    summary="List and create crops",
)
class CropListCreateView(generics.ListCreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset.order_by('-id')


@extend_schema(
    tags=["Crops"],
    summary="Retrieve, update, and delete crop",
)
class CropDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset.order_by('-id')