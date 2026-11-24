from django.contrib import admin
from apps.crops.models import Crop

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_bn', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'name_bn')
    list_filter = ('is_active',)