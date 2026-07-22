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
        transcript_data = ytt.fetch(video_id, languages=['en']) # sends request to Youtube to fetch English transcript for given video_id

        full_text = " ".join([entry.text for entry in transcript_data]) # joins all segments together into one continuous readable paragraph
        return full_text        #returns formatted paragraph
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"       # converts error into readable message

if __name__ == "__main__":      #code block runs when executed in cmd
        youtube_url = input("Enter YouTube URL: \n")
        transcript = get_youtube_transcript(youtube_url)
        print("\n--- TRANSCRIPT ---\n")
        print(transcript[:500] + "...\n[Truncated]")