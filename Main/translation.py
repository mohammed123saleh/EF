from modeltranslation.translator import translator, TranslationOptions
from .models import Item, Variation

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Item, NewsTranslationOptions)





class VariationTra(TranslationOptions):
    fields = ('Title',)

translator.register(Variation, VariationTra)