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
