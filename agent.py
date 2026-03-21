import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(system_prompt, user_message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

def agent_for(topic, opponent_argument=None):
    if opponent_argument:
        user_msg = f"Topic: {topic}\n\nYour opponent just said:\n\"{opponent_argument}\"\n\nRespond directly to what they said. Quote or reference their specific claim, then tear it apart. Speak like a real person in a debate, not an essay. 2-3 sentences max."
    else:
        user_msg = f"Topic: {topic}\n\nGive your opening argument FOR this topic. Speak like a confident person, not a formal essay. 2-3 sentences."
    
    return call_llm(
        "You are in a live debate. Speak naturally and conversationally. Never start with 'The notion' or formal essay language.",
        user_msg
    )

def agent_against(topic, opponent_argument=None):
    if opponent_argument:
        user_msg = f"Topic: {topic}\n\nYour opponent just said:\n\"{opponent_argument}\"\n\nRespond directly to what they said. Quote or reference their specific claim, then tear it apart. Speak like a real person in a debate, not an essay. 2-3 sentences max."
    else:
        user_msg = f"Topic: {topic}\n\nGive your opening argument AGAINST this topic. Speak like a confident person, not a formal essay. 2-3 sentences."
    
    return call_llm(
        "You are in a live debate. Speak naturally and conversationally. Never start with 'The notion' or formal essay language.",
        user_msg
    )
    

def agent_judge(topic, arg_for, arg_against):
    return call_llm(
        "You are an impartial debate judge. Score both arguments on logic, clarity, and persuasiveness (out of 10). Use line breaks between each criterion. End with a clear winner declaration on a new line. Do not use markdown formatting or asterisks.",
        f"Topic: {topic}\n\nArgument FOR:\n{arg_for}\n\nArgument AGAINST:\n{arg_against}"
    )

if __name__ == "__main__":
    topic = "AI will replace software engineers"
    print("FOR:\n", agent_for(topic))
    print("\nAGAINST:\n", agent_against(topic))