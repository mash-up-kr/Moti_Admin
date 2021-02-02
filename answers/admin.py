from django.contrib import admin
from rangefilter.filter import DateTimeRangeFilter

from answers.models import Answer

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_content",
        "imageUrl",
        "date",
        "setDate",
        "no",
        "missionId",
        "fileId",
        "userId",
        "createdAt",
        "updatedAt",
    )
    list_display_links = ("short_content",)
    fields = (
        "imageUrl",
        "content",
        "no",
        "missionId",
        "fileId",
        "userId",
    )
    readonly_fields = (
        "date",
        "setDate",
        "createdAt",
        "updatedAt",
    )
    list_select_related = (
        "fileId",
        "missionId",
        "userId",
    )
    raw_id_fields = (
        "fileId",
        "missionId",
        "userId",
    )
    list_filter = (
        "fileId__part",
        "missionId"
    )
    search_fields = (
        "userId__email__exact",
        ('createdAt', DateTimeRangeFilter),
    )