from django.contrib import admin
from apps.crops.models import(
    Crop,CropSeason,
    CropVariety,CropCycle
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

@admin.register(CropVariety)
class CropVarietyAdmin(admin.ModelAdmin):
    list_display = ('crop','name','name_bn','id','is_active','created_at','updated_at')

@admin.register(CropCycle)
class CropCycleAdmin(admin.ModelAdmin):
    list_display = ('farmer','land','crop','variety','season','id')