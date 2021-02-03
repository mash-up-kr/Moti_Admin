from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class Parts(models.Model):
    cardUrl = models.URLField(
        max_length=255,
        default="",
        null=False,
        verbose_name=_("파츠 PDF 주소"),
    )
    cardSvgUrl = models.URLField(
        max_length=255,
        default="",
        null=False,
        verbose_name=_("파츠 SVG 주소"),
    )
    cardPngUrl = models.URLField(
        max_length=255,
        default="",
        null=False,
        verbose_name=_("파츠 PNG 주소"),
    )
    part = models.PositiveIntegerField(
        default=0,
        verbose_name=_("파츠 번호"),
    )
    createdAt = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("생성 날짜"),
    )
    updatedAt = models.DateTimeField(
        auto_now=True,
        verbose_name=_("수정 날짜"),
    )

    class Meta:
        managed = False
        db_table = "files"
        verbose_name = _("파츠 목록")
        verbose_name_plural = _("파츠 목록")

    def __str__(self):
        return f"No. {self.part}"

    def card_pdf_url_tag(self):
        return mark_safe(
            '<embed src="{}#toolbar=0" width="240px" style="height: 404px" />'.format(
                self.cardUrl
            )
        )

    card_pdf_url_tag.short_description = "파츠 PDF 이미지"
    card_pdf_url_tag.allow_tags = True

    def card_png_url_small_tag(self):
        return mark_safe(
            '<img src="{}" width="160px" style="border: 1px dotted #666;" />'.format(
                self.cardPngUrl
            )
        )

    card_png_url_small_tag.short_description = "파츠 PNG 작은 이미지"
    card_png_url_small_tag.allow_tags = True

    def card_png_url_tag(self):
        return mark_safe(
            '<img src="{}" width="240px" style="border: 1px dotted #666;" />'.format(
                self.cardPngUrl
            )
        )

    card_png_url_tag.short_description = "파츠 PNG 이미지"
    card_png_url_tag.allow_tags = True

    def card_svg_url_tag(self):
        return mark_safe(
            '<embed src= "{}#toolbar=0" width="240px" height="404px" type="image/svg+xml" />'.format(
                self.cardUrl
            )
        )

    card_svg_url_tag.short_description = "파츠 SVG 이미지"
    card_svg_url_tag.allow_tags = True
