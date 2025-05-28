import requests
import pandas as pd
import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# ======== YOUR CONFIGURATION ========
ASSET_ID = "awsrgDXSJeyN6GDn8U2Qmm"  # Your asset ID
KOBO_BASE_URL = "https://kf.kobotoolbox.org"  # Verify your Kobo server URL
# ====================================

def main():
    try:
        # Get API token from environment
        API_TOKEN = os.environ.get("KOBO_API_TOKEN")
        if not API_TOKEN:
            raise ValueError("KOBO_API_TOKEN environment variable not set!")
            
        # Build API URL
        api_url = f"{KOBO_BASE_URL}/api/v2/assets/{ASSET_ID}/data.json"
        logger.info(f"Fetching data from: {api_url}")
        
        # Make API request
        headers = {"Authorization": f"Token {API_TOKEN}"}
        response = requests.get(api_url, headers=headers, timeout=30)
        
        # Check response
        if response.status_code != 200:
            error_msg = f"API error {response.status_code}: {response.text[:200]}"
            logger.error(error_msg)
            raise ConnectionError(error_msg)
            
        # Process data
        data = response.json().get("results", [])
        if not data:
            logger.warning("No data received from API")
            return
            
        # Convert to CSV
        df = pd.json_normalize(data)
        csv_path = os.path.join(os.getcwd(), "kobo_data.csv")
        df.to_csv(csv_path, index=False)
        logger.info(f"Success! Saved {len(df)} records to {csv_path}")
        
        # Verify file creation
        if not os.path.exists(csv_path):
            raise FileNotFoundError("CSV file not created after save operation!")
            
    except Exception as e:
        logger.exception("Critical error occurred:")
        sys.exit(1)

if __name__ == "__main__":
    main()
