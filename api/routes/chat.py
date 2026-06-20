from fastapi import APIRouter

router = APIRouter()

@router.get("/chat")
def contract_chat():
    return {
        "status": "success",
        "message": "Contract chatbot endpoint ready"
    }