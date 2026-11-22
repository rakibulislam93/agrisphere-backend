from django.contrib import admin
from apps.accounts.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','phone_number', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
