from django.contrib import admin
from rangefilter.filter import DateTimeRangeFilter

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "name",
        "gender",
        "birthday",
        "refreshDate",
        "refreshToken",
        "mission",
        "snsId",
        "snsType",
        "createdAt",
        "updatedAt",
    )
    fields = (
        "email",
        "name",
        "gender",
        "birthday",
        "snsId",
        "snsType",
    )
    readonly_fields = (
        "refreshDate",
        "refreshToken",
        "mission",
        "createdAt",
        "updatedAt",
    )
    search_fields = ("email__exact", "snsId__exact",)
    list_filter = (
        ('createdAt', DateTimeRangeFilter),
    )