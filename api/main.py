from fastapi import FastAPI

app = FastAPI(
    title="AI-Powered Contract Intelligence & Risk Scoring"
)

@app.get("/")
def home():
    return {"message": "API is running successfully"}