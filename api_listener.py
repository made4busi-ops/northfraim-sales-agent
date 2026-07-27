from flask import Flask, request, jsonify
import json
import subprocess

app = Flask(__name__)

@app.route('/new_lead', methods=['POST'])
def catch_lead():
    # 1. Catch the lead data from the internet
    lead_data = request.json
    if not lead_data:
        return jsonify({"error": "No data received"}), 400

    print(f"\n[WEBHOOK] Lead caught! Name: {lead_data.get('lead_name')}")

    # 2. Save it to the file the Brain reads
    with open('lead_data.json', 'w') as f:
        json.dump(lead_data, f, indent=2)

    # 3. Trigger the Master Orchestrator in the background
    print("[WEBHOOK] Firing Master Orchestrator...")
    subprocess.Popen(['python3', 'master_orchestrator.py'])

    return jsonify({"status": "Lead received and pipeline started!"}), 200

if __name__ == '__main__':
    print("=== EARS ACTIVATED: LISTENING FOR LEADS ON PORT 5000 ===")
    app.run(host='0.0.0.0', port=5000)
