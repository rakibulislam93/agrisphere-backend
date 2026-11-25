from rest_framework import generics
from apps.crops.models import CropCycle
from apps.crops.serializers import(
    CropCycleCreateUpdateSerializer,
    CropCycleListSerializer
)
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from apps.farmers.permissions import IsActiveFarmer
from apps.common.views import FarmerBaseView
from apps.common.pagination import CustomPageNumberPagination



@extend_schema(
    tags=["Crops"],
    summary="List and create crop cycles",
)
class CropCycleListCreateView(FarmerBaseView, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsActiveFarmer]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CropCycleCreateUpdateSerializer
        return CropCycleListSerializer

    def get_queryset(self):
        farmer = self.get_farmer()

        qs = CropCycle.objects.select_related(
            'land', 'crop', 'variety', 'season'
        ).filter(farmer=farmer)

        return qs.order_by('-id')


    def perform_create(self, serializer):
        serializer.save(farmer=self.get_farmer())



@extend_schema(
    tags=["Crops"],
    summary="Retrieve, update, and delete crop cycle",
)
class CropCycleDetailView(
    FarmerBaseView,
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated, IsActiveFarmer]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return CropCycleCreateUpdateSerializer
        return CropCycleListSerializer

    def get_queryset(self):
        farmer = self.get_farmer()

        qs = CropCycle.objects.select_related(
            'land', 'crop', 'variety', 'season'
        ).filter(farmer=farmer)

        return qs.order_by('-id')