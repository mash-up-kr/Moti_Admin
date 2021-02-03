from django.contrib import admin
from rangefilter.filter import DateTimeRangeFilter

from questions.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = (
        "id",
        "content",
        "createdAt",
        "updatedAt",
    )
    list_display_links = ("content",)
    fields = ("content",)
    readonly_fields = (
        "createdAt",
        "updatedAt",
    )
    list_filter = (("createdAt", DateTimeRangeFilter),)
