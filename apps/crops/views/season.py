from rest_framework import generics
from apps.crops.models import CropSeason
from apps.crops.serializers import CropSeasonSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAdminUser

@extend_schema(
    tags=["Crops"],
    summary="List and create crop seasons",
)
class CropSeasonListCreateView(generics.ListCreateAPIView):
    queryset = CropSeason.objects.all()
    serializer_class = CropSeasonSerializer
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset.order_by('-id')


@extend_schema(
    tags=["Crops"],
    summary="Retrieve, update, and delete crop season",
)
class CropSeasonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CropSeason.objects.all()
    serializer_class = CropSeasonSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset.order_by('-id')