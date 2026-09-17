from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai import ask_ai

app = FastAPI(
    title="Akash AI API",
    description="Backend API for Akash AI Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "app": "Akash AI",
        "status": "online",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api/features")
def features():
    return {
        "chat": True,
        "image_edit": True,
        "image_generation": True,
        "web_search": True,
        "music": True,
        "file_analysis": True
    }


@app.post("/api/chat")
def chat(request: ChatRequest):
    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    answer = ask_ai(message)

    return {
        "success": True,
        "message": message,
        "answer": answer
    }
