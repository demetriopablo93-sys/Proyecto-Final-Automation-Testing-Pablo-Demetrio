import json
import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / 'data'

def load_json(path: str):
    with open(DATA_DIR / path) as f:
        return json.load(f)


def load_csv(path: str):
    rows = []
    with open(DATA_DIR / path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows