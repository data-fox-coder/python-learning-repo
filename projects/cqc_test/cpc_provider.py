"""
CQC Provider — Syndication API
================================================
Loads provider data from CQC API and loads into a .csv file. This file will then be loaded into Snowflake as Snowflake trial account does not allow direct API access.

Requires:
    CQC_API_KEY set as a Codespaces secret (or in a .env file)

Usage:
    python cqc_api_test.py
"""

import os

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

CQC_API_KEY = os.environ["CQC_API_KEY"]

response = requests.get(
    "https://api.service.cqc.org.uk/public/v1/providers/1-101716203",
    headers={"Ocp-Apim-Subscription-Key": CQC_API_KEY},
    timeout=30,
)

response.raise_for_status()

data = response.json()

provider_df = pd.DataFrame([data])

provider_df = provider_df.explode("locationIds")

provider_df = provider_df.rename(columns={"locationIds": "locationId"})

provider_df.to_csv("cqc_provider.csv", index=False)

print(provider_df)