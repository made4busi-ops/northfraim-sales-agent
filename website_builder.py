import os

def build_website(lead_data):
    print("\n=== WIRING: BRAIN TALKING TO ARCHITECT (WEBSITE BUILDER) ===")
    tier = lead_data.get('tier')
    company = lead_data.get('lead_company', 'Your Company')
    
    # Format the company name for the file
    safe_name = company.replace(" ", "_").lower()
    
    if tier == 'TIER_3':
        print("[ARCHITECT] Tier 3 detected. Generating LUXURY website...")
        # Luxury Code (Dark mode, gold accents, cinematic)
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{company} | Luxury Experience</title>
    <style>
        body {{ margin: 0; background-color: #0a0a0a; color: #fff; font-family: 'Segoe UI', sans-serif; }}
        .hero {{ height: 100vh; display: flex; justify-content: center; align-items: center; text-align: center; border-bottom: 2px solid #d4af37; }}
        h1 {{ font-size: 64px; color: #d4af37; text-transform: uppercase; letter-spacing: 4px; }}
        p {{ font-size: 24px; color: #ccc; max-width: 600px; margin: 20px auto; }}
        .cta {{ padding: 15px 40px; background: transparent; border: 2px solid #d4af37; color: #d4af37; font-size: 18px; cursor: pointer; text-transform: uppercase; }}
    </style>
</head>
<body>
    <div class="hero">
        <div>
            <h1>{company}</h1>
            <p>Experience the pinnacle of quality. Hollywood-grade service for those who demand the best.</p>
            <button class="cta">Schedule a Private Call</button>
        </div>
    </div>
</body>
</html>"""
        file_path = os.path.expanduser(f"~/northfraim-job77/logs/{safe_name}_luxury_site.html")
        
    else:
        print("[ARCHITECT] Tier 1/2 detected. Generating FREE lead-magnet website...")
        # Basic Code (Clean, white, simple)
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{company}</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
        h1 {{ color: #333; }}
        a {{ display: inline-block; margin-top: 20px; padding: 10px 20px; background: #007BFF; color: white; text-decoration: none; }}
    </style>
</head>
<body>
    <h1>Welcome to {company}</h1>
    <p>Your free basic website is ready. Want to upgrade to a luxury cinematic site?</p>
    <a href="#">Contact Us to Upgrade</a>
</body>
</html>"""
        file_path = os.path.expanduser(f"~/northfraim-job77/logs/{safe_name}_free_site.html")

    # Save the file
    with open(file_path, 'w') as f:
        f.write(html_content)
        
    print(f"[ARCHITECT] Website successfully built and saved to: {file_path}")

