"""Quick sanity check for the T-100 CSV before running the notebook.

Usage (from the repo root):  python scripts/check_data.py
"""
from pathlib import Path
import sys

import pandas as pd

CSV = Path(__file__).resolve().parents[1] / "data" / "T_T100D_SEGMENT_ALL_CARRIER.csv"
REQUIRED = ["ORIGIN", "DEST", "CLASS", "DEPARTURES_PERFORMED", "PASSENGERS"]

if not CSV.exists():
    sys.exit(f"Missing file: {CSV}\nSee data/README.md for download instructions.")

df = pd.read_csv(CSV, usecols=lambda c: c in REQUIRED)
missing = [c for c in REQUIRED if c not in df.columns]
if missing:
    sys.exit(f"The CSV is missing required columns: {missing}")

print(f"OK: {len(df):,} rows, all required columns present.")
print("CLASS values found:", sorted(df["CLASS"].dropna().unique()))
