from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.utils import extend_schema

from apps.accounts.views import(
    RegistrationView,
    LoginView,
    LogoutView,
    PasswordChangeView,
    CustomTokenRefreshView,
)


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),

]