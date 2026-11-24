from rest_framework.permissions import BasePermission


class IsActiveFarmer(BasePermission):
    message = "User does not have an active farmer profile."

    def has_permission(self, request, view):
        farmer = getattr(request.user, "farmer_profile", None)

        return farmer is not None and farmer.is_active