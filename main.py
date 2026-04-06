from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Chat App is running"}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "AI Chat App is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message.lower()

    if "hello" in user_message:
        reply = "Hello! How can I help you today?"
    elif "job" in user_message:
        reply = "I can help you with resumes, projects, and interview prep."
    elif "ai" in user_message:
        reply = "AI can be used to build tools that solve real-world problems."
    else:
        reply = f"You said: {request.message}"

    return {"response": reply}
