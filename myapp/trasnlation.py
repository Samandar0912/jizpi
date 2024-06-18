from modeltranslation.translator import register, TranslationOptions
from .models import ArticleNews, ArticleElon, ArticleKafedra

@register(ArticleNews)
class ArticleNewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(ArticleElon)
class ArticleElonTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(ArticleKafedra)
class ArticleKafedraTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'name', 'qabul', 'text')
