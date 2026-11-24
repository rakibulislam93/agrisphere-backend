from django.urls import path
from apps.crops.views import (
    CropListCreateView,
    CropDetailView,
)

urlpatterns = [

    path("", CropListCreateView.as_view(), name="crop-list"),
    path("<int:pk>/", CropDetailView.as_view(), name="crop-detail"),

]