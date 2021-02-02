from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AnswersConfig(AppConfig):
    name = 'answers'
    verbose_name = _("답변")
