from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import transcript

app = FastAPI(title="SaaS YouTube & Audio Transcription API", version="1.0.0")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(transcript.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    