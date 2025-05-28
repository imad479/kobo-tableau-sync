import requests
import pandas as pd
import os
import sys

# ======== REPLACE THESE VALUES ========
ASSET_ID = "awsrgDXSJeyN6GDn8U2Qmm"  # e.g. "aBc123dEf456gHi789jKl"
API_TOKEN = os.environ.get("edac13bbcd3ba6d893c5881597e740a338e2ca1a")  # Set in GitHub Secrets
# ======================================

def main():
    try:
        # 1. Fetch data from Kobo Toolbox
        url = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_ID}/data.json"
        headers = {"Authorization": f"Token {API_TOKEN}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad status
        
        # 2. Process data
        data = response.json().get("results", [])
        if not data:
            print("No data received from Kobo")
            return
            
        # 3. Convert to CSV
        df = pd.json_normalize(data)
        df.to_csv("kobo_data.csv", index=False)
        print(f"Success! Created CSV with {len(df)} records")
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        sys.exit(1)  # Fail the workflow

if __name__ == "__main__":
    main()
