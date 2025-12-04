## CS598 Project - Seokhyun Lee (sl251@illinois.edu)
# student-performance-curation 
Curation of a Student Performance Dataset for Educational Analytics
This repository contains the data curation workflow developed for **Foundations of Data Curation**.

## Project Overview
Goal: Curate and anonymize the *Student Performance* dataset for privacy-preserving educational analysis.

## Folder Structure
- `data/raw/`: Original dataset
- `data/processed/`: Cleaned and de-identified data
- `scripts/`: Python scripts for cleaning, privacy, and metadata
- `metadata/`: Data dictionary and DataCite metadata
- `logs/`: Provenance log
- `docs/`: Project documents (proposal, progress, final report)

## How to Reproduce
1. Run `scripts/cleaning.py`
2. Run `scripts/privacy_transform.py`
3. Run `scripts/metadata_generator.py`
4. Run `scripts/provenance_log.py`

Each run regenerates the curated dataset and documentation for reproducibility.

# Student Performance Data Curation Pipeline

*CS598 Foundations of Data Curation – Final Project*
*Author: Seokhyun (Jason) Lee (sl251)*

## 1. Introduction

This project implements a reproducible data‑curation pipeline that transforms the raw *Students Performance* dataset into a cleaned, de‑identified, metadata‑rich, and provenance‑tracked dataset.

Running the pipeline automatically produces:

* Cleaned dataset
* De‑identified dataset
* Metadata JSON + codebook
* UUID‑based identifier record
* Analytics summary
* Provenance log of all operations

Run the full workflow:

```
python main.py
```

## 2. Repository Structure

```
.
├── main.py
├── cleaning.py
├── privacy_transform.py
├── metadata_generator.py
├── analysis_summary.py
├── identifier_system.py
├── provenance_log.py
├── data/
│   ├── raw/
│   │   └── StudentsPerformance.csv
│   ├── processed/
│   ├── metadata/
│   └── analytics/
└── logs/
    └── provenance_log.txt
```

## 3. Installation

Install required packages:

```
pip install pandas numpy matplotlib
```

(Optional) activate virtual environment before installing.

## 4. Running the Pipeline

Ensure this file exists:

```
data/raw/StudentsPerformance.csv
```

Then run:

```
python main.py
```

Outputs will be created in:

```
data/processed/
data/metadata/
data/analytics/
logs/
```

## 5. Pipeline Components

### Cleaning (`cleaning.py`)

* Strips whitespace
* Fills missing values
* Normalizes categories
* Validates numeric fields
  Output: `data/processed/StudentsPerformance_clean.csv`

### Privacy Transformation (`privacy_transform.py`)

Removes direct identifiers (name, address, phone, etc.).
Output: `data/processed/StudentsPerformance_deidentified.csv`

### Metadata Generation (`metadata_generator.py`)

Creates codebook + metadata JSON describing variables, schema, and dataset.
Outputs:

```
data/metadata/codebook.csv
data/metadata/metadata.json
```

### Identifier System (`identifier_system.py`)

Generates persistent UUID metadata.
Output: `data/metadata/identifier.json`

### Analysis Summary (`analysis_summary.py`)

Performs descriptive analysis.
Output: `data/analytics/analysis_report.txt`

### Provenance Logging (`provenance_log.py`)

Records every step: inputs, outputs, timestamps, transformations.
Output: `logs/provenance_log.txt`

## 6. Output Summary

Running `main.py` produces:

```
data/processed/StudentsPerformance_clean.csv
data/processed/StudentsPerformance_deidentified.csv
data/metadata/codebook.csv
data/metadata/metadata.json
data/metadata/identifier.json
data/analytics/analysis_report.txt
logs/provenance_log.txt
```

## 7. Troubleshooting

* **Dataset not found:** Verify file exists at `data/raw/StudentsPerformance.csv`.
* **Import errors:** Run from project root (`python main.py`).
* **File overwrite:** Pipeline overwrites processed data but appends provenance logs.

## 8. Extending the Pipeline

To add a new module:

1. Create new script file
2. Log actions with `write_provenance()`
3. Add call inside `main.py`
4. Update documentation

## 9. License

Created for UIUC CS598 Foundations of Data Curation coursework. Academic use only.

