from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.service import DiscussionAnalysisService
import os

app = FastAPI(title="Discussion Analysis AI Service")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize service
service = DiscussionAnalysisService()


@app.get("/")
def read_root():
    return {"message": "Discussion Analysis AI Service", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_discussion(request: AnalysisRequest):
    """Analyze a discussion and return insights"""
    try:
        if not request.messages:
            raise HTTPException(status_code=400, detail="No messages provided")
        
        result = service.analyze_discussion(request)
        return result
        
    except Exception as e:
        print(f"Error analyzing discussion: {e}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
