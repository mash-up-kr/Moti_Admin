from django.contrib import admin
from rangefilter.filter import DateTimeRangeFilter

from answers.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_content",
        "preview_image_url",
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
        "content",
        "no",
        "missionId",
        "fileId",
        "userId",
        "imageUrl",
        "content_image_url",
    )
    readonly_fields = (
        "content_image_url",
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