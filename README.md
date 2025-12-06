# Student Performance Data Curation Pipeline  
**CS598: Foundations of Data Curation – Final Project**  
**Author:** Seokhyun (Jason) Lee (sl251@illinois.edu)

## Overview
This repository implements a fully automated, reproducible data‑curation workflow for the *Student Performance* dataset.  
The pipeline performs:

- Data cleaning & validation  
- Privacy transformation (PII removal + binning)  
- Metadata & codebook generation  
- UUID‑based identifier assignment  
- Provenance logging  
- Analytic verification (correlations, plots, summary)  
- FAIR‑aligned dataset organization  

Run the entire workflow:

```bash
python main.py
```

---

## Repository Structure

```
.
├── main.py
├── scripts/
│   ├── cleaning.py
│   ├── privacy_transform.py
│   ├── metadata_generator.py
│   ├── provenance_log.py
│   └── analysis_summary.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── curated/
├── metadata/
│   ├── metadata.json
│   └── codebook.csv
├── logs/
│   └── provenance_log.txt
└── analysis/
    ├── correlation_heatmap.png
    ├── scatter_studytime_gpa.png
    ├── correlation_table.csv
    └── summary.txt
```

---

## Workflow Summary

### **1. Cleaning**
`scripts/cleaning.py`  
- Normalizes column names  
- Fixes types and ranges  
- Removes duplicates and invalid records  
Output: `StudentsPerformance_clean.csv`

### **2. Privacy Transformation**
`scripts/privacy_transform.py`  
- Removes synthetic PII (Name, SSN, Address, PhoneNumber, StudentID)  
- Applies GPA/Age binning  
- Ensures quasi-identifier safety (k ≈ 5)  
Output: `StudentsPerformance_deidentified.csv`

### **3. Metadata Generation**
`scripts/metadata_generator.py`  
- Creates `metadata.json` using schema.org/DataCite  
- Generates `codebook.csv` with variable definitions

### **4. Provenance Logging**
`scripts/provenance_log.py`  
- Records every pipeline action  
- Stores timestamps and transformations in `logs/provenance_log.txt`

### **5. Analytic Verification**
`scripts/analysis_summary.py`  
- Computes correlations  
- Generates validation plots  
- Confirms analytic value is preserved

---

## Reproducibility

The entire workflow runs deterministically:

```bash
python main.py
```

Every run produces identical curated outputs and updates provenance logs for transparency.

---

## FAIR Compliance

- **Findable:** Metadata uses schema.org/DataCite  
- **Accessible:** Public repository with clear structure  
- **Interoperable:** Standardized CSV + JSON‑LD formats  
- **Reusable:** Complete documentation, codebook, and provenance

---

## License
MIT License (or update if required by your course)

---

## Citation
If referencing this curated dataset or workflow, please cite your final report or GitHub repository.

