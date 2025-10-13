## CS598 Foundation of Data Curation 
## Seokhyun Lee (sl251@illinois.edu)
# scripts/metadata_generator.py
import pandas as pd
import json
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.provenance_log import write_provenance


input_path = "data/processed/StudentsPerformance_deidentified.csv"
meta_dir = "data/processed/metadata"
os.makedirs(meta_dir, exist_ok=True)

print(f"Loading dataset from: {input_path}")
df = pd.read_csv(input_path)

# --- Step 1: Generate data dictionary ---
codebook = pd.DataFrame({
    "Column": df.columns,
    "DataType": [str(df[c].dtype) for c in df.columns],
    "Description": [
        "Age of student (15–18 years)",
        "Gender (0=Male, 1=Female)",
        "Ethnicity code (0–3)",
        "Parental education level (0–4)",
        "Weekly study time in hours",
        "Absences during school year",
        "Tutoring (0=No, 1=Yes)",
        "Parental support (0–4)",
        "Extracurricular (0=No, 1=Yes)",
        "Sports participation (0=No, 1=Yes)",
        "Music participation (0=No, 1=Yes)",
        "Volunteering (0=No, 1=Yes)",
        "GPA (0.0–4.0)",
        "Grade classification (0–4)"
    ][:len(df.columns)]
})
codebook.to_csv(f"{meta_dir}/codebook.csv", index=False, encoding="utf-8-sig")

# --- Step 2: Generate JSON metadata (DataCite style) ---
metadata = {
    "@context": "https://schema.org/",
    "@type": "Dataset",
    "name": "Student Performance Dataset (Deidentified)",
    "creator": {"name": "Seokhyun (Jason) Lee", "affiliation": "UIUC"},
    "description": "This dataset captures demographic, study, and activity factors influencing GPA and grade classification.",
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "version": "1.0",
    "keywords": ["education", "student performance", "GPA", "machine learning"],
    "datePublished": pd.Timestamp.now().strftime("%Y-%m-%d"),
    "variableMeasured": list(df.columns),
    "distribution": {
        "@type": "DataDownload",
        "encodingFormat": "text/csv",
        "contentUrl": "data/processed/StudentsPerformance_deidentified.csv"
    }
}
with open(f"{meta_dir}/metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=4)

print(f"Metadata and codebook saved under {meta_dir}")

# --- Provenance ---
write_provenance(
    "Metadata Generation",
    f"Created data dictionary (codebook.csv) and JSON metadata (metadata.json) "
    f"for dataset {input_path} with {df.shape[1]} variables."
)