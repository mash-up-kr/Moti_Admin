from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from files.models import Parts
from missions.models import Mission
from users.models import User


class Answer(models.Model):
    imageUrl = models.URLField(
        max_length=255,
        default='',
        null=True,
        verbose_name=_("첨부 이미지파일 주소"),
    )

    content = models.TextField(
        default='',
        null=False,
        verbose_name=_("주관식 답변 내용"),
    )

    date = models.DateField(
        auto_now=True,
        verbose_name=_("파츠 지급 날짜")
    )

    setDate = models.DateField(
        auto_now=True,
        verbose_name=_("파츠 첫 생성 날짜")
    )

    no = models.IntegerField(
        default=0,
        null=False,
        verbose_name=_("파츠 번호"),
    )

    missionId = models.ForeignKey(
        Mission,
        null=True,
        related_name="missions_answers",
        on_delete=models.SET_NULL,
        verbose_name=_("미션"),
        db_column="missionId",
    )

    fileId = models.ForeignKey(
        Parts,
        null=True,
        related_name="parts_answers",
        on_delete=models.SET_NULL,
        verbose_name=_("파츠"),
        db_column="fileId",
    )

    userId = models.ForeignKey(
        User,
        null=True,
        related_name="users_answers",
        on_delete=models.SET_NULL,
        verbose_name=_("유저"),
        db_column="userId",
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
        db_table = "answers"
        verbose_name = _("답변 목록")
        verbose_name_plural = _("답변 목록")

    @property
    def short_content(self):
        return truncatechars(self.content, 35)
    short_content.fget.short_description = _("주관식 답변 내용")

    def preview_image_url(self):
        if self.imageUrl is not None:
            return mark_safe('<img src="{}" width="240px" style="border: 1px dotted #666;" />'.format(self.imageUrl))
        return "-"
    preview_image_url.short_description = "첨부 이미지 파일 미리보기"
    preview_image_url.allow_tags = True

    def content_image_url(self):
        return mark_safe('<img src="{}" style="border: 1px dotted #666;" />'.format(self.imageUrl))
    content_image_url.short_description = "첨부 이미지 파일"
    content_image_url.allow_tags = True