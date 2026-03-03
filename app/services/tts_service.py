from gtts import gTTS
import uuid

class TTSService:
    def generate(self, text: str, lang: str):
        filename = f"temp_audio_{uuid.uuid4()}.mp3"
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        return filename