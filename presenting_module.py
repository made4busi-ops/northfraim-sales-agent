def present(lead_data):
    print("\n--- PRESENTING (Ries Position & YC Acquisition) ---")
    tier = lead_data.get('tier')
    
    if tier == 'TIER_1':
        lead_data['positioning'] = "SPEED (First movie in 30 seconds)"
        lead_data['acquisition'] = "Social, viral, content marketing"
    elif tier == 'TIER_2':
        lead_data['positioning'] = "OWNERSHIP (Your face. Your voice. Only you.)"
        lead_data['acquisition'] = "Email, existing users, word-of-mouth"
    else:
        lead_data['positioning'] = "QUALITY (Hollywood quality. Your story. Your crew.)"
        lead_data['acquisition'] = "Direct sales, partnerships, case studies"
        
    print(f"[Ries] Locked Word: {lead_data['positioning']}")
    print(f"[YC] Acquisition Channel: {lead_data['acquisition']}")
    return lead_data
