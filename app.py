import re   #regular expression module
from youtube_transcript_api import YouTubeTranscriptApi     # imports YouTubeTranscriptApi class from youtube-transcript-api package: handles requests to YouTube to pull data without downloading video

# Takes youtube URL string as input and returns the 11-character video ID string
def extract_video_id(url: str) -> str:
    pattern = r"(?:v|\/)([0-9A-Za-z_-]{11})"    #regex pattern matching
    match = re.search(pattern, url)             # searches the provided URL against the pattern, if found returns an object
    if not match:       
        raise ValueError("Invalid YouTube URL")         #throws exception error if link provided is invalid
    return match.group(1)           # Extracts and returns the captured 11-char ID string from regex group

# Takes youtube URL and returns combined full text of transcript
def get_youtube_transcript(url: str) -> str:
    try:
        video_id = extract_video_id(url)

        ytt = YouTubeTranscriptApi()    #API wrapper object
        transcript_data = ytt.fetch(video_id, languages=['en'])

        full_text = " ".join([entry['text'] for entry in transcript_data])
        return full_text
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"