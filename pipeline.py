import json
import os
import sqlite3
from database import get_config, init_db

def wait_for_human_approval(phase, lead_data):
    config = get_config()
    if not config['pipeline']['require_human_approval']:
        return True
        
    print(f"\n--- HUMAN APPROVAL GATE: {phase.upper()} ---")
    print(f"Lead: {lead_data.get('lead_name')} at {lead_data.get('lead_company')}")
    print(f"Data: {json.dumps(lead_data, indent=2)}")
    
    while True:
        choice = input("Approve to continue to next phase? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            print("[GATE] Approved. Moving forward...")
            return True
        elif choice in ['no', 'n']:
            print("[GATE] Rejected. Halting pipeline.")
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def run_pipeline(lead_data):
    init_db()
    config = get_config()
    db_path = os.path.expanduser(config['database']['path'])
    table = config['database']['table']
    
    print("\n=== STARTING SALES PIPELINE ===")
    
    # 1. Prospecting
    print("\n[1/5] Running Prospecting Module...")
    import prospecting_module
    lead_data = prospecting_module.prospect(lead_data)
    if not wait_for_human_approval("Prospecting", lead_data): return
    
    # 2. Qualifying
    print("\n[2/5] Running Qualifying Module...")
    import qualifying_module
    lead_data = qualifying_module.qualify(lead_data)
    if not wait_for_human_approval("Qualifying", lead_data): return
    
    # 3. Presenting
    print("\n[3/5] Running Presenting Module...")
    import presenting_module
    lead_data = presenting_module.present(lead_data)
    if not wait_for_human_approval("Presenting", lead_data): return
    
    # 4. Objection Handling
    print("\n[4/5] Running Objection Module...")
    import objection_module
    lead_data = objection_module.handle_objections(lead_data)
    if not wait_for_human_approval("Objection Handling", lead_data): return
    
    # 5. Closing
    print("\n[5/5] Running Closing Module...")
    import closing_module
    lead_data = closing_module.close(lead_data)
    if not wait_for_human_approval("Closing", lead_data): return
    
    # Save to DB
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f'''
        INSERT INTO {table} (lead_name, lead_company, tier, prospect_score, 
        budget_answer, authority_answer, need_answer, timeline_answer, process_answer, 
        qualification_score, current_phase)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''', (
        lead_data.get('lead_name'), lead_data.get('lead_company'), lead_data.get('tier'),
        lead_data.get('prospect_score'), lead_data.get('budget_answer'),
        lead_data.get('authority_answer'), lead_data.get('need_answer'),
        lead_data.get('timeline_answer'), lead_data.get('process_answer'),
        lead_data.get('qualification_score'), 'completed'
    ))
    conn.commit()
    conn.close()
    print("\n[SUCCESS] Pipeline completed. Lead saved to 'sales_pipeline' table.")

if __name__ == "__main__":
    # Load lead data and run
    with open('lead_data.json', 'r') as f:
        lead = json.load(f)
    run_pipeline(lead)
