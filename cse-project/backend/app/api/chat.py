from fastapi import APIRouter, HTTPException
from app.models.chat import Message, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/message", response_model=ChatResponse)
async def process_message(message: Message):
    try:
        response = await chat_service.process_message(message)
        return ChatResponse(
            message=response,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))