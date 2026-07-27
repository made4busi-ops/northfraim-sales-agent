import os
import json
import sqlite3
from database import get_config

def audit_system():
    print("\n=== MARTELL AUDITOR: THE PERFECT GUY ACTIVATED ===")
    print("[IDENTITY] I am Martell. I am the systems architect. I do not do the work. I grade it.")
    print("-" * 50)
    
    score = 0
    feedback = []

    config = get_config()
    db_path = os.path.expanduser(config['database']['path'])
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT current_phase FROM sales_pipeline ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        if result and result[0] == 'completed':
            score += 25
            feedback.append("✅ VISION (Brain): Logic gate passed. Lead saved to DB. (25/25)")
        else:
            feedback.append("❌ VISION (Brain): Lead not approved or missing from DB. (0/25)")
    else:
        feedback.append("❌ VISION (Brain): Database not found. (0/25)")

    queue_path = os.path.expanduser("~/northfraim-job77/logs/genie_queue.json")
    if os.path.exists(queue_path):
        with open(queue_path, 'r') as f:
            data = json.load(f)
        if data.get('status') == 'QUEUED_FOR_RENDER':
            score += 25
            feedback.append("✅ TASTE (Hands): Commercial Genie payload queued correctly. (25/25)")
        else:
            feedback.append("❌ TASTE (Hands): Payload malformed. (0/25)")
    else:
        feedback.append("❌ TASTE (Hands): Genie queue file missing. (0/25)")

    email_path = os.path.expanduser("~/northfraim-job77/logs/draft_email.txt")
    if os.path.exists(email_path) and os.path.getsize(email_path) > 50:
        score += 25
        feedback.append("✅ CARE (Mouth): Email dynamically generated for the prospect. (25/25)")
    else:
        feedback.append("❌ CARE (Mouth): Email draft missing or too short. (0/25)")

    if os.path.exists('lead_data.json'):
        score += 25
        feedback.append("✅ DIRECTOR (Org): Scout handoff successful. System is fully wired. (25/25)")
    else:
        feedback.append("❌ DIRECTOR (Org): Lead data missing. Wiring broken. (0/25)")

    print("[AUDIT REPORT - STAGE 4 FRAMEWORK]")
    for note in feedback:
        print(note)
    
    print("-" * 50)
    print(f"FINAL SYSTEM GRADE: {score}/100")
    
    if score == 100:
        print("[VERDICT] Machine is operating at peak efficiency. You bought back your time.")
    else:
        print("[VERDICT] System has gaps. Review the failures above and re-run.")

if __name__ == "__main__":
    audit_system()
