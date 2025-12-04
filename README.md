# Student Performance Data Curation Pipeline  
**CS598: Foundations of Data Curation – Final Project**  
**Author:** Seokhyun (Jason) Lee (sl251@illinois.edu)

---

## 1. Project Overview

This repository contains a fully automated, reproducible data-curation workflow for the **Students Performance** dataset.  
The pipeline performs:

- Data cleaning and validation  
- Deterministic privacy transformation  
- Metadata + codebook generation  
- UUID-based identifier creation  
- Analytical verification  
- Provenance tracking for every step  

Run the entire workflow with:

```bash
python main.py
