from django.db import models
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    content = models.CharField(
        max_length=255,
        default='',
        null=False,
        verbose_name=_("질문 내용"),
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
        db_table = "questions"
        verbose_name = _("수집 질문 목록")
        verbose_name_plural = _("수집 질문 목록")
