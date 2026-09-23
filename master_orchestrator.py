import json
import os
import requests
from pipeline import run_pipeline
from database import get_config
import website_builder

def trigger_commercial_genie(lead_data):
    print("\n=== WIRING: BRAIN TALKING TO HANDS ===")
    tier = lead_data.get('tier')
    positioning = lead_data.get('positioning', 'Default Pitch')
    lead_name = lead_data.get('lead_name')

    job_payload = {
        "project_name": f"Pitch Video for {lead_name}",
        "target_tier": tier,
        "script_angle": positioning,
        "status": "QUEUED_FOR_RENDER"
    }

    queue_path = os.path.expanduser("~/northfraim-sales-agent/logs/genie_queue.json")
    with open(queue_path, 'w') as f:
        json.dump(job_payload, f, indent=2)
        
    print(f"[ORCHESTRATOR] Job sent to Commercial Genie!")
    print(f"[ORCHESTRATOR] Payload: {json.dumps(job_payload)}")

def generate_email_with_llm(lead_data):
    print("\n=== WIRING: BRAIN TALKING TO MOUTH (OPENROUTER) ===")
    config = get_config()
    api_key = config['api'].get('openrouter_key', 'missing')
    
    if api_key == 'missing' or "YOUR_KEY_HERE" in api_key:
        print("[LLM] API Key not set in config.json. Skipping email generation.")
        return

    lead_name = lead_data.get('lead_name')
    lead_company = lead_data.get('lead_company')
    positioning = lead_data.get('positioning')
    need = lead_data.get('need_answer')
    timeline = lead_data.get('timeline_answer')
    
    prompt = f"Write a short, punchy cold email to {lead_name} at {lead_company}. They mentioned their need is: '{need}' and timeline is '{timeline}'. Our pitch angle is: '{positioning}'. Write the email to directly address their need using our pitch angle. No fluff. Include a placeholder for the video link [VIDEO_LINK]."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "openai/gpt-oss-20b:free",
        "messages": [
            {"role": "system", "content": "You are an expert sales copywriter. You write direct, high-converting emails based on the provided context."},
            {"role": "user", "content": prompt}
        ]
    }
    
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        email_text = response.json()['choices'][0]['message']['content']
        
        print("[LLM] Email Draft Generated:")
        print("-" * 40)
        print(email_text)
        print("-" * 40)
        
        email_path = os.path.expanduser("~/northfraim-sales-agent/logs/draft_email.txt")
        with open(email_path, 'w') as f:
            f.write(email_text)
            
        print(f"[ORCHESTRATOR] Email saved to {email_path}")
    except Exception as e:
        print(f"[LLM] Error connecting to OpenRouter: {e}")

if __name__ == "__main__":
    with open('lead_data.json', 'r') as f:
        lead = json.load(f)

    print("=== MASTER ORCHESTRATOR ACTIVATED ===")
    run_pipeline(lead)

    if lead.get('close_status') == 'APPROVED':
        print("\n[ORCHESTRATOR] Brain approved the lead. Triggering all organs...")
        trigger_commercial_genie(lead)
        website_builder.build_website(lead)
        generate_email_with_llm(lead)
    else:
        print("\n[ORCHESTRATOR] Brain rejected or halted. Do not trigger organs.")
