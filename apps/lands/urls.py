from django.urls import path
from apps.lands.views import (
    LandListCreateView,
    LandDetailView,
)

urlpatterns = [
    path("", LandListCreateView.as_view(), name="land-list-create"),
    path("<int:pk>/", LandDetailView.as_view(), name="land-detail"),

]