## CS598 Foundation of Data Curation 
## Seokhyun Lee (sl251@illinois.edu)

from datetime import datetime
import os

def write_provenance(stage, details):
    os.makedirs("logs", exist_ok=True)
    log_path = "logs/provenance_log.txt"

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n=== Provenance Log Entry ===\n")
        f.write(f"Timestamp: {datetime.now()}\n")
        f.write(f"Stage: {stage}\n")
        f.write(f"Details:\n{details}\n")
        f.write(f"--- End Entry ---\n")

    print(f"***Provenance log updated*** → {log_path}")