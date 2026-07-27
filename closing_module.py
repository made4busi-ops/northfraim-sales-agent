def close(lead_data):
    print("\n--- CLOSING (Albada Logic Gate) ---")
    tier = lead_data.get('tier')
    score = lead_data.get('qualification_score', 0)
    
    if tier and score > 80:
        lead_data['close_status'] = "APPROVED"
        print("[Albada] Tier clear, Math works, Message aligned. Logic Gate: APPROVED.")
    else:
        lead_data['close_status'] = "ESCALATE"
        print("[Albada] Logic Gate: FAILED - Escalate to Derrick.")
    return lead_data
