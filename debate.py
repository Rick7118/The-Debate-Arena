from agent import agent_for, agent_against, agent_judge

def run_debate(topic, rounds=3):
    debate_log = []
    last_for = None
    last_against = None

    for round_num in range(1, rounds + 1):
        arg_for = agent_for(topic, last_against)      # reads opponent's last argument
        arg_against = agent_against(topic, last_for)  # reads opponent's last argument

        debate_log.append({"round": round_num, "for": arg_for, "against": arg_against})
        last_for = arg_for
        last_against = arg_against

    full_for = "\n".join([f"Round {r['round']}: {r['for']}" for r in debate_log])
    full_against = "\n".join([f"Round {r['round']}: {r['against']}" for r in debate_log])
    verdict = agent_judge(topic, full_for, full_against)

    return {"rounds": debate_log, "verdict": verdict}

    # Judge evaluates the full debate
    full_for = "\n".join([f"Round {r['round']}: {r['for']}" for r in debate_log])
    full_against = "\n".join([f"Round {r['round']}: {r['against']}" for r in debate_log])

    print("\n--- Judge's Verdict ---")
    verdict = agent_judge(topic, full_for, full_against)
    print(verdict)

    return {"rounds": debate_log, "verdict": verdict}

if __name__ == "__main__":
    run_debate("AI will replace software engineers", rounds=3)