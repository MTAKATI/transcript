from app.services.base import TranscriptStrategy
from app.services.youtube import YouTubeTranscriptStrategy

class TranscriptServiceFactory:
    @staticmethod
    def get_service(source_type: str) -> TranscriptStrategy:
        if source_type.lower() in ["youtube", "youtube_url"]:
            return YouTubeTranscriptStrategy()

        # Future Expansion Examples
        # elif source_type.lower() == "whisper":
        #    return OpenAIWhisperStrategy()

        raise ValueError(f"Unsupported transcription source type: '{source_type}'")