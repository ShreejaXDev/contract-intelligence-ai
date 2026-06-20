from fastapi import FastAPI

from api.routes.upload import router as upload_router
from api.routes.analyze import router as analyze_router
from api.routes.chat import router as chat_router

app = FastAPI(
    title="AI-Powered Contract Intelligence & Risk Scoring",
    version="1.0.0"
)

# Include route modules
app.include_router(upload_router)
app.include_router(analyze_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "AI-Powered Contract Intelligence API is running successfully"
    }