from agent import agent_for, agent_against, agent_judge

def run_debate(topic, rounds=3):
    debate_log = []

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")

        arg_for = agent_for(topic)
        arg_against = agent_against(topic)

        print(f"FOR: {arg_for}")
        print(f"AGAINST: {arg_against}")

        debate_log.append({
            "round": round_num,
            "for": arg_for,
            "against": arg_against
        })

    # Judge evaluates the full debate
    full_for = "\n".join([f"Round {r['round']}: {r['for']}" for r in debate_log])
    full_against = "\n".join([f"Round {r['round']}: {r['against']}" for r in debate_log])

    print("\n--- Judge's Verdict ---")
    verdict = agent_judge(topic, full_for, full_against)
    print(verdict)

    return {"rounds": debate_log, "verdict": verdict}

if __name__ == "__main__":
    run_debate("AI will replace software engineers", rounds=3)