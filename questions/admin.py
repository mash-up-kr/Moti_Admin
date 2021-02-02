from django.contrib import admin
from rangefilter.filter import DateTimeRangeFilter

from questions.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "createdAt",
        "updatedAt",
    )
    fields = (
        "content",
    )
    readonly_fields = (
        "createdAt",
        "updatedAt",
    )
    list_filter = (
        ('createdAt', DateTimeRangeFilter),
    )