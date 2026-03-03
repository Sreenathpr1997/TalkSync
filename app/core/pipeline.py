from app.services.stt_service import STTService
from app.services.translation_service import TranslationService
from app.services.tts_service import TTSService

class TalkSyncPipeline:
    def __init__(self):
        self.stt = STTService()
        self.translator = TranslationService()
        self.tts = TTSService()

    def process(self, audio_path: str, source_lang: str, target_lang: str):
        transcript = self.stt.transcribe(audio_path)
        translated = self.translator.translate(transcript, source_lang, target_lang)
        audio_output = self.tts.generate(translated, target_lang)

        return transcript, translated, audio_output