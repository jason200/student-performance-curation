## CS598 Foundation of Data Curation 
## Seokhyun Lee (sl251@illinois.edu)

# scripts/privacy_transform.py
import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.provenance_log import write_provenance


input_path = "data/processed/StudentsPerformance_clean.csv"
output_path = "data/processed/StudentsPerformance_deidentified.csv"

os.makedirs("data/processed", exist_ok=True)

print(f"Loading dataset from: {input_path}")
df = pd.read_csv(input_path)

# --- Step 1: Confirm and remove potential identifiers ---
direct_identifiers = [
    col for col in df.columns
    if col.strip().lower() in ["studentid", "ssn", "address", "phonenumber", "studentname"]
]

if direct_identifiers:
    print(f"Removing remaining identifiers: {direct_identifiers}")
    df.drop(columns=direct_identifiers, inplace=True)
else:
    print("No direct identifiers found — dataset already deidentified by ARX.")

# --- Step 2: Save ---
df.to_csv(output_path, index=False, encoding="utf-8-sig")
print(f"Deidentified dataset saved: {output_path}")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# --- Provenance ---
write_provenance(
    "Privacy Transformation",
    f"Loaded {input_path}, verified removal of identifiers ({direct_identifiers or 'none'}), "
    f"and saved deidentified dataset to {output_path} (Rows={df.shape[0]}, Cols={df.shape[1]})."
)