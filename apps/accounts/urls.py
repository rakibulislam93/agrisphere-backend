from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from apps.accounts.views import(
    RegistrationView,
    LoginView,
    LogoutView,
    PasswordChangeView
)


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LoginView.as_view(), name='logout')

]