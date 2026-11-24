from django.contrib import admin
from apps.lands.models import Land

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ('id','name','farmer','area','location','is_active')