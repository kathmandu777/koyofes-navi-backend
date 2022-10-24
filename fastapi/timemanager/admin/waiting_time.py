from django.contrib import admin

from ..models import WaitingTime


@admin.register(WaitingTime)
class WaitingTimeAdmin(admin.ModelAdmin):
    list_display = ("exhibit", "minutes", "created_at")
    list_filter = ("exhibit",)
