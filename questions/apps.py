from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class QuestionsConfig(AppConfig):
    name = 'questions'
    verbose_name = _('수집 질문')

