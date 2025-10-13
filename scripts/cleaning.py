## CS598 Foundation of Data Curation 
## Seokhyun Lee (sl251@illinois.edu)
# scripts/cleaning.py
import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.provenance_log import write_provenance

input_path = "data/raw/StudentsPerformance.csv"
output_path = "data/processed/StudentsPerformance_clean.csv"

os.makedirs("data/processed", exist_ok=True)
print(f"Loading dataset from: {input_path}")
df = pd.read_csv(input_path)

# --- Step 1: Basic cleaning ---
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

# Fill missing values
df.fillna({
    'Gender': 0,
    'ParentalSupport': 2,
    'ParentalEducation': 2
}, inplace=True)

# --- Step 2: Standardize encodings ---
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].replace({'M': 0, 'F': 1, 'Male': 0, 'Female': 1}).astype(int)

if 'ParentalEducation' in df.columns:
    df['ParentalEducation'] = df['ParentalEducation'].clip(lower=0, upper=4).astype(int)

# --- Step 3: Validate ranges ---
for col, (lo, hi) in {
    "Absences": (0, 30),
    "GPA": (0.0, 4.0),
    "Age": (15, 18),
    "StudyTimeWeekly": (0, 30)
}.items():
    if col in df.columns:
        df[col] = df[col].clip(lower=lo, upper=hi)

# --- Step 4: Output cleaned dataset ---
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"Cleaned dataset saved: {output_path}")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# --- Provenance ---
write_provenance(
    "Cleaning",
    f"Loaded raw file {input_path}, normalized encodings, validated ranges, saved cleaned dataset → {output_path} "
    f"(Rows={df.shape[0]}, Cols={df.shape[1]})"
)