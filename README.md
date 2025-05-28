# Kobo Toolbox to Tableau Sync

Automated data pipeline that syncs Kobo Toolbox data to GitHub for Tableau Public.

## Setup
1. Add your KoboToolbox API token as a GitHub Secret (`KOBO_API_TOKEN`)
2. Set your asset ID in `sync_kobo.py`
3. Workflow runs daily at midnight UTC

## Workflow
1. GitHub Actions fetches data from Kobo API
2. Converts JSON to CSV
3. Commits updated CSV to repository

## Connect to Tableau Public
Use this URL:  
`https://raw.githubusercontent.com/imad479/kobo-tableau-sync/main/kobo_data.csv`
