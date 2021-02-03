from django.db import models
from django.utils.translation import gettext_lazy as _


class Mission(models.Model):
    title = models.URLField(
        max_length=255,
        default="",
        null=False,
        verbose_name=_("미션 제목"),
    )
    isContent = models.BooleanField(
        default=False,
        verbose_name=_("주관식"),
    )
    isImage = models.BooleanField(default=False, verbose_name=_("사진"))
    cycle = models.PositiveIntegerField(default=0, null=False, verbose_name=_("미션 주기"))
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
        db_table = "missions"
        verbose_name = _("미션 목록")
        verbose_name_plural = _("미션 목록")

    def __str__(self):
        return f"{self.title}"
