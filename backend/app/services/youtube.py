import re
from youtube_transcript_api import YouTubeTranscriptApi
from app.services.base import TranscriptStrategy

class YouTubeTranscriptStrategy(TranscriptStrategy):

    def extract_video_id(self, url: str) -> str:
        pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
        match = re.search(pattern, url)
        if not match:
            raise ValueError("Invalid YouTube URL format.")
        return match.group(1)

    def get_transcript(self, source: str) -> str:
        video_id = self.extract_video_id(source)
        ytt = YouTubeTranscriptApi()
        transcript_data = ytt.fetch(video_id, languages=['en'])

        # Access snippet object attributes using dot notation (.text)
        return " ".join([entry.text for entry in transcript_data])
    