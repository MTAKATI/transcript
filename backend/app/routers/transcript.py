from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.factory import TranscriptServiceFactory

router = APIRouter(prefix="/api/transcript", tags=["Transcript"])

class TranscriptRequest(BaseModel):
    url: str
    source_type: str = "youtube"        # Default source type 

@router.post("/")
def create_transcript(request: TranscriptRequest):
    try:
        # Obtain strategy from Factory
        service = TranscriptServiceFactory.get_service(request.source_type)

        # Execute strategy
        transcript_text = service.get_transcript(request.url)

        return {
            "status": "success",
            "source_type": request.source_type,
            "transcript": transcript_text
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process transcript: {str(2)}")