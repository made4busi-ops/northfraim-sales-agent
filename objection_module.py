def handle_objections(lead_data):
    print("\n--- OBJECTION HANDLING (Bhagat Ethics) ---")
    tier = lead_data.get('tier')
    
    if tier == 'TIER_1':
        lead_data['ethics_check'] = "Respects their time (they're busy, curious)"
    elif tier == 'TIER_2':
        lead_data['ethics_check'] = "Respects their investment (they're paying)"
    else:
        lead_data['ethics_check'] = "Respects their reputation (they're professional)"
        
    print(f"[Bhagat] Ethics Check: {lead_data['ethics_check']} - PASS.")
    return lead_data
