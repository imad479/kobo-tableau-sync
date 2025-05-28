import os
print(f"Current working directory: {os.getcwd()}")
print(f"Absolute path to CSV: {os.path.abspath('kobo_data.csv')}")
import requests
import pandas as pd
import os
import logging

# Setup logging
logging.basicConfig(filename='kobo_sync.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # KoboToolbox API settings
    API_TOKEN = os.environ.get(edac13bbcd3ba6d893c5881597e740a338e2ca1a)
    ASSET_ID = "awsrgDXSJeyN6GDn8U2Qmm"  # REPLACE WITH YOUR ACTUAL ASSET ID
    KOBO_URL = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_ID}/data.json"
    
    logging.info(f"API Token: {API_TOKEN[:5]}...")  # Log first 5 chars
    logging.info(f"API URL: {KOBO_URL}")
    
    # Fetch data from KoboToolbox
    headers = {'Authorization': f'Token {API_TOKEN}'}
    response = requests.get(KOBO_URL, headers=headers)
    
    logging.info(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json().get('results', [])
        logging.info(f"Received {len(data)} records")
        
        if data:
            df = pd.json_normalize(data)
            df.to_csv('kobo_data.csv', index=False)
            logging.info("CSV file created successfully")
        else:
            logging.warning("No data received from API")
    else:
        logging.error(f"API Error: {response.text[:200]}")

except Exception as e:
    logging.exception("An error occurred:")
  df.to_csv('C:/Users/HP/Documents/kobo-tableau-sync/kobo_data.csv', index=False)
