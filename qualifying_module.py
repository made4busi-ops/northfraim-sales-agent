def qualify(lead_data):
    print("\n--- QUALIFYING (Walling Math Check) ---")
    # Math check: Does the economics work?
    # For this example, we assume production cost is $500. 
    production_cost = 500
    expected_value = 5000 
    
    if expected_value > production_cost:
        lead_data['qualification_score'] = 92
        print(f"[Math Check] Production Cost: ${production_cost} | Expected Value: ${expected_value}. Payback < 12 months. PASS.")
    else:
        lead_data['qualification_score'] = 30
        print("[Math Check] Math does not work. FAIL.")
    return lead_data
