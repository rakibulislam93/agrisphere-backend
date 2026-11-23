from django.urls import path

from apps.farmers.views import (
    FarmerProfileCreateView,
    FarmerProfileRetrieveUpdateView,
    FarmerProfileDeactivateView,
    FarmerProfileActivateView,
)
app_name = "farmers"

urlpatterns = [
    path(
        "profile/",
        FarmerProfileCreateView.as_view(),
        name="profile-create",
    ),
    path(
        "profile/me/",
        FarmerProfileRetrieveUpdateView.as_view(),
        name="profile-retrieve-update",
    ),
    path(
        "profile/me/deactivate/",
        FarmerProfileDeactivateView.as_view(),
        name="profile-deactivate",
    ),
    path(
        "profile/me/activate/",
        FarmerProfileActivateView.as_view(),
        name="profile-activate",
    ),


]