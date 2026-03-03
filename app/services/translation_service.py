from deep_translator import GoogleTranslator

class TranslationService:
    def translate(self, text: str, source_lang: str, target_lang: str):
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)