# The Debate Arena

A multi-agent AI system where two LLM agents argue opposing sides of any topic, and a judge agent evaluates the debate and declares a winner.

**Live demo**: https://the-debate-arena.vercel.app

## How it works

Three specialized agents powered by Llama 3.3 (via Groq) are orchestrated in a debate loop:

- **Agent For** — argues in favor of the topic
- **Agent Against** — argues against the topic
- **Judge Agent** — scores both sides on logic, clarity, and persuasiveness, then declares a winner

Each agent is the same LLM given a different system prompt — demonstrating how role-based prompting enables multi-agent behavior from a single model.

## Tech stack

- **Backend**: FastAPI, Python
- **LLM**: mixtral-8x7b-32768
- **Frontend**: React + Vite
- **Deployment**: Railway (backend), Vercel (frontend)

## Run locally

clone the repo, create a .env file with GROQ_API_KEY=your_key, then:

    cd The-Debate-Arena
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload

    cd frontend
    npm install
    npm run dev

## Known limitations

- Agents do not always directly reference the opponent's specific points — this is a limitation of open-source models defaulting to essay-style responses rather than true rebuttal behavior
- Cold start on Railway free tier can cause a delay of a few seconds on the first request

## Model

Currently using `mixtral-8x7b-32768` via Groq. Multi-LLM selector (letting users choose the model for each agent) is planned for v2.
