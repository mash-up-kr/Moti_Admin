from django.db import models
from django.utils.translation import gettext_lazy as _

from files.models import Parts
from missions.models import Mission

class SexChoices(models.TextChoices):
    """ 성별 목록 """

    FEMALE = "여", "여자"
    MALE = "남", "남자"

class User(models.Model):

    SEX_CHOICES = (
        ("남", "남자"),
        ("여", "여자"),
    )

    birthday = models.DateField(
        null=True,
        verbose_name=_("생년월일")
    )

    email = models.CharField(
        max_length=255,
        default='',
        null=False,
        verbose_name=_("이메일"),
    )

    name = models.CharField(
        max_length=255,
        default='',
        null=True,
        verbose_name=_("이름"),
    )

    gender = models.CharField(
        max_length=255,
        choices=SexChoices.choices,
        default=SexChoices.FEMALE,
        null=True,
        verbose_name=_("성별"),
    )

    refreshDate = models.DateField(
        auto_now=True,
        null=True,
        verbose_name=_("새로 고침 날짜")
    )

    refreshToken = models.CharField(
        max_length=255,
        default='',
        null=True,
        verbose_name=_("이름"),
    )

    mission = models.TextField(
        default='',
        null=True,
        verbose_name=_("미션 JSON"),
    )

    snsId = models.CharField(
        max_length=255,
        default='',
        null=False,
        verbose_name=_("소셜 아이디"),
    )

    snsType = models.CharField(
        max_length=255,
        default='',
        null=False,
        verbose_name=_("소셜 타입"),
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
        db_table = "users"
        verbose_name = _("유저 목록")
        verbose_name_plural = _("유저 목록")

    def __str__(self):
        return f"{self.email}"