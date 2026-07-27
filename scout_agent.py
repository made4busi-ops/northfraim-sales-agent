import json
import subprocess
import time
import os

def hunt_and_fire():
    print("=== SCOUT AGENT: THE HUNTER ACTIVATED ===")
    print("[IDENTITY] I am Scout. I am the eyes of Northfraim. My job is to find the water.")
    time.sleep(2)
    
    target_lead = {
        "lead_name": "Marcus Cole",
        "lead_company": "Apex Logistics",
        "budget_answer": "$50K",
        "authority_answer": "I am the CEO",
        "need_answer": "We need training videos for our drivers, current production takes 6 weeks",
        "timeline_answer": "Need them by end of Q3",
        "process_answer": "Quality and clarity are everything"
    }

    print(f"[SCOUT] Target acquired: {target_lead['lead_name']} at {target_lead['lead_company']}")
    
    with open('lead_data.json', 'w') as f:
        json.dump(target_lead, f, indent=2)
        
    print("[DEFINITION OF DONE] Lead acquired. Data packaged. Handoff to Brain initiated...")
    print("-" * 50)
    
    subprocess.run(['python3', 'master_orchestrator.py'])

if __name__ == "__main__":
    hunt_and_fire()
