from abc import ABC, abstractmethod 

class TranscriptStrategy(ABC):
    @abstractmethod
    def get_transcript(self, source: str) -> str:
        """Extracts transcript text from a source (URL or File path)"""
        pass