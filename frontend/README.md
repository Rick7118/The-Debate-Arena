# The Debate Arena

A multi-agent AI system where two LLM agents argue opposing sides of any topic, and a judge agent evaluates the debate and declares a winner.

**Live demo**: https://the-debate-arena.vercel.app

## How it works

Three specialized agents powered by Llama 3.3 (via Groq) are orchestrated in a debate loop:

- **Agent For** — argues in favor of the topic
- **Agent Against** — argues against the topic  
- **Judge Agent** — scores both sides on logic, clarity, and persuasiveness, then declares a winner

Each agent is the same LLM given a different system prompt — demonstrating how role-based prompting enables multi-agent behavior from a single model.

## Architecture
```
User input (topic)
       ↓
  For each round:
    Agent For → argument
    Agent Against → argument
       ↓
  Judge Agent → scores + verdict
       ↓
  React frontend displays results
```

## Tech stack

- **Backend**: FastAPI, Python
- **LLM**: Llama 3.3 70B via Groq API
- **Frontend**: React + Vite
- **Deployment**: Railway (backend), Vercel (frontend)

## Run locally
```bash
# Backend
git clone https://github.com/Rick7118/The-Debate-Arena.git
cd The-Debate-Arena
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "GROQ_API_KEY=your_key_here" > .env
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```