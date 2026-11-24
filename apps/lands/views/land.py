from rest_framework import generics
from apps.lands.models import Land
from apps.lands.serializers import(
    LandCreateUpdateSerializer,
    LandSerializer
)
from apps.farmers.permissions import IsActiveFarmer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from apps.common.pagination import CustomPageNumberPagination

@extend_schema(
    tags=["Lands"],
    summary="List and create lands",
)
class LandListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsActiveFarmer]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LandCreateUpdateSerializer
        return LandSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Land.objects.select_related(
            'farmer__user'
        ).filter(farmer__user=user)

        return qs.order_by('-id')

    def perform_create(self, serializer):
        serializer.save(
            farmer=self.request.user.farmer_profile
        )



@extend_schema(
    tags=["Lands"],
    summary="Retrieve, update, and delete land",
)
class LandDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated, IsActiveFarmer]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return LandCreateUpdateSerializer
        return LandSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Land.objects.select_related(
            'farmer__user'
        ).filter(farmer__user=user)

        return qs.order_by('-id')


        