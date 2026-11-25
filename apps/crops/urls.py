from django.urls import path
from apps.crops.views import (
    CropListCreateView,
    CropDetailView,
    # crop season views
    CropSeasonListCreateView,
    CropSeasonDetailView,

    # crop variety views
    CropVarietyListCreateView,
    CropVarietyDetailView,

    # crop cycle views
    CropCycleListCreateView,
    CropCycleDetailView,
)

urlpatterns = [

    path("", CropListCreateView.as_view(), name="crop-list"),
    path("<int:pk>/", CropDetailView.as_view(), name="crop-detail"),
    path("seasons/", CropSeasonListCreateView.as_view(), name="crop-season-list"),
    path("seasons/<int:pk>/", CropSeasonDetailView.as_view(), name="crop-season-detail"),

    path("varieties/", CropVarietyListCreateView.as_view(), name="crop-variety-list"),
    path("varieties/<int:pk>/", CropVarietyDetailView.as_view(), name="crop-variety-detail"),

    path("cycles/", CropCycleListCreateView.as_view(), name="crop-cycle-list"),
    path("cycles/<int:pk>/", CropCycleDetailView.as_view(), name="crop-cycle-detail"),

]