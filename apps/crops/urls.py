from django.urls import path
from apps.crops.views import (
    CropListCreateView,
    CropDetailView,
    # crop season views
    CropSeasonListCreateView,
    CropSeasonDetailView,
)

urlpatterns = [

    path("", CropListCreateView.as_view(), name="crop-list"),
    path("<int:pk>/", CropDetailView.as_view(), name="crop-detail"),
    path("seasons/", CropSeasonListCreateView.as_view(), name="crop-season-list"),
    path("seasons/<int:pk>/", CropSeasonDetailView.as_view(), name="crop-season-detail"),


]