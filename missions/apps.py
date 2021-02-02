from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MissionsConfig(AppConfig):
    name = 'missions'
    verbose_name = _("미션")
