from faster_whisper import WhisperModel
from app.config import MODEL_SIZE, DEVICE

class STTService:
    def __init__(self):
        self.model = WhisperModel(MODEL_SIZE, device=DEVICE)

    def transcribe(self, audio_path: str) -> str:
        segments, _ = self.model.transcribe(audio_path)
        text = ""
        for segment in segments:
            text += segment.text + " "
        return text.strip()