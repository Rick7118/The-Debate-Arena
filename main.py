from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from debate import run_debate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DebateRequest(BaseModel):
    topic: str
    rounds: int = 3

@app.options("/debate")
async def options_debate():
    return JSONResponse(content={}, headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "*",
    })

@app.post("/debate")
def debate(req: DebateRequest):
    result = run_debate(req.topic, req.rounds)
    return result