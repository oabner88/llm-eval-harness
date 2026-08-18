import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "source_of_truth.json"


def get_record(campaign_id):
    records = json.loads(DATA_PATH.read_text())
    for record in records:
        if record["campaign_id"] == campaign_id:
            return record
    raise KeyError(f"No record found for campaign_id={campaign_id!r}")
