"""
CQC Test — Syndication API
================================================
Extracts data from the CQC Syndication API and saves it to a list of dictionaries for testing purposes. 
Data will be loaded into a Snowflake table once testing is complete.

Requires:
    CQC_API_KEY set as a Codespaces secret (or in a .env file)

Usage:
    python cqc_api_test.py
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

CQC_API_KEY = os.environ["CQC_API_KEY"]

response = requests.get(
    "https://api.service.cqc.org.uk/public/v1/providers/1-101716203",
    headers={'Ocp-Apim-Subscription-Key': CQC_API_KEY},
)

response.raise_for_status()

data = response.json()

print(data)