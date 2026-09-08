"""
CQC Location — Syndication API
================================================
Loads location data from CQC API and loads into a .csv file for a location and its reports, showing each CQC report as a new row in a second .csv file.

This file will then be loaded into Snowflake as Snowflake trial account does not allow direct API access.

Due to the structure of the data, this requires a fan-out API call to show each report as a new row in the resulting .csv file.

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
    "https://api.service.cqc.org.uk/public/v1/locations/1-111561368",
    headers={"Ocp-Apim-Subscription-Key": CQC_API_KEY},
    timeout=30,
)

response.raise_for_status()

data = response.json()

# print(data.keys())

location_df = pd.DataFrame([data])

reports_df = pd.json_normalize(
    data,                    # original dict
    record_path="reports",
    meta=["locationId"],
    errors="ignore"
)

location_df.to_csv("cqc_location.csv", index=False)                                                              
reports_df.to_csv("cqc_reports.csv", index=False)

# Print the dataframes for sense checking and to verify that the reports have been extracted correctly
print(location_df)
print(reports_df)
print(reports_df.shape)
