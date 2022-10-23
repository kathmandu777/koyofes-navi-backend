from django.contrib import admin

from ..models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "position_x", "position_y")
    search_fields = ("name",)
    list_filter = ("image",)
