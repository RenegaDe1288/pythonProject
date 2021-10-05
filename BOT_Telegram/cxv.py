from translate import Translator
translator= Translator(from_lang = 'ru',to_lang="en")
translation = translator.translate("Подольск",)
print(translation)