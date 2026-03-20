from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from debate import run_debate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://the-debate-arena.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DebateRequest(BaseModel):
    topic: str
    rounds: int = 3

@app.post("/debate")
def debate(req: DebateRequest):
    result = run_debate(req.topic, req.rounds)
    return result