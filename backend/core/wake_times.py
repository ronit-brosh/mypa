import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data" / "wakeup_times.json"


def load_wakeup_times():
    with open(DATA_PATH, "r") as f:
        return json.load(f)
