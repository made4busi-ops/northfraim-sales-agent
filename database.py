import json
import os
import sqlite3

def get_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def init_db():
    config = get_config()
    db_path = os.path.expanduser(config['database']['path'])
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales_pipeline (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_name TEXT, lead_company TEXT, tier TEXT,
            prospect_score INTEGER, budget_answer TEXT, authority_answer TEXT,
            need_answer TEXT, timeline_answer TEXT, process_answer TEXT,
            qualification_score INTEGER, current_phase TEXT
        )
    ''')
    conn.commit()
    conn.close()
