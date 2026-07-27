def prospect(lead_data):
    print("\n--- PROSPECTING (Walling Tier Lock) ---")
    budget_str = lead_data.get('budget_answer', '')
    
    # Pricing Research Logic
    if '50K' in budget_str or '50,000' in budget_str:
        lead_data['tier'] = 'TIER_3'
        lead_data['market_value'] = "$10,000 - $50,000"
        lead_data['our_price'] = "$125/min"
        print("[Market Research] Budget indicates Tier 3. Market rate: $10k+. Our price: $125/min. Value: High.")
    elif '5K' in budget_str:
        lead_data['tier'] = 'TIER_2'
        lead_data['market_value'] = "$2,000 - $10,000"
        lead_data['our_price'] = "$35-$50 add-on"
        print("[Market Research] Budget indicates Tier 2. Market rate: $2k+. Our price: $50 add-on. Value: High.")
    else:
        lead_data['tier'] = 'TIER_1'
        lead_data['market_value'] = "$500 - $2,000"
        lead_data['our_price'] = "$5-$49"
        print("[Market Research] Budget indicates Tier 1. Market rate: $500+. Our price: $29. Value: 98% less cost.")
        
    lead_data['prospect_score'] = 100
    return lead_data
