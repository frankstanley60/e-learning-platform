# user_interaction/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import Content
from .models import Exercise


@register(Content)
class ContentTranslationOptions(TranslationOptions):
    field = ('content_pretty_name')  # Add more fields as needed
