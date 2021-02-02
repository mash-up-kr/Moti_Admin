from django.contrib import admin
from rangefilter.filter import DateTimeRangeFilter

from files.models import Parts


@admin.register(Parts)
class PartsAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = (
        "card_png_url_small_tag",
        "part",
        "createdAt",
        "updatedAt",
    )
    fields = (
        "part",
        "cardUrl",
        "card_pdf_url_tag",
        "cardPngUrl",
        "card_png_url_tag",
        "cardSvgUrl",
        "card_svg_url_tag",
    )
    readonly_fields = (
        "card_pdf_url_tag",
        "card_png_url_tag",
        "card_svg_url_tag",
        "createdAt",
        "updatedAt",
    )
    list_filter = (
        "part",
        ('createdAt', DateTimeRangeFilter),
    )
