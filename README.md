# Kobo Toolbox to Tableau Sync

Automated pipeline that syncs Kobo data to GitHub for Tableau Public.

## Setup
1. Set GitHub Secret: `KOBO_API_TOKEN` with your Kobo API token
2. Verify asset ID in `sync_kobo.py`
3. Workflow runs daily at midnight UTC

## Connect Tableau
Use this URL:  
`https://raw.githubusercontent.com/imad479/kobo-tableau-sync/main/kobo_data.csv`
[![Download Data](https://img.shields.io/badge/Download-Data-green)](https://raw.githubusercontent.com/your-username/kobo-repo/main/data/kobo_data.csv)
