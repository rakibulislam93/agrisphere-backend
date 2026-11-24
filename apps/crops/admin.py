from django.contrib import admin
from apps.crops.models import(
    Crop,CropSeason
)

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_bn', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'name_bn')
    list_filter = ('is_active',)
@admin.register(CropSeason)
class CropSeasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'crop', 'name', 'name_bn', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'name_bn')
    list_filter = ('is_active',)