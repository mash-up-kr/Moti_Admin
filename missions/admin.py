from django.contrib import admin
from rangefilter.filter import DateTimeRangeFilter

from missions.models import Mission


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "isContent",
        "isImage",
        "cycle",
        "createdAt",
        "updatedAt",
    )
    fields = (
        "title",
        "isContent",
        "isImage",
        "cycle",
    )
    readonly_fields = (
        "createdAt",
        "updatedAt",
    )
    list_filter = (
        "isContent",
        "isImage",
        ('createdAt', DateTimeRangeFilter),
    )