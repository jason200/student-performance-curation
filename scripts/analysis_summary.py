## CS598 Foundation of Data Curation 
## Seokhyun Lee (sl251@illinois.edu)
# analysis_summary.py
"""
analysis_summary.py
Analytic Verification of Curated Dataset
----------------------------------------
Inputs:
    data/processed/StudentsPerformance_deidentified.csv
Outputs:
    data/analytics/analysis_report.txt
    data/analytics/gpa_relationships.png
    data/analytics/gpa_correlations.csv
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.provenance_log import write_provenance


# --- Setup ---
IN_FILE = "data/processed/StudentsPerformance_deidentified.csv"
os.makedirs("data/analytics", exist_ok=True)

if not os.path.exists(IN_FILE):
    print(f"Missing input file: {IN_FILE}")
    write_provenance("Analysis Verification", "Skipped - missing deidentified dataset.")
    exit(1)

# --- Step 1: Load curated data ---
df = pd.read_csv(IN_FILE)
print(f"Loaded deidentified dataset with {df.shape[0]} records and {df.shape[1]} columns")

# --- Step 2: Select variables for correlation analysis ---
numeric_vars = [
    "Age", "Gender", "Ethnicity", "ParentalEducation", "StudyTimeWeekly",
    "Absences", "Tutoring", "ParentalSupport", "Extracurricular",
    "Sports", "Music", "Volunteering", "GradeClass"
]

# Keep only valid numeric columns that exist in the dataset
numeric_vars = [v for v in numeric_vars if v in df.columns]
corr_vars = ["GPA"] + numeric_vars

# --- Step 3: Correlation analysis ---
corr_matrix = df[corr_vars].corr(method="pearson")

# Save to CSV for transparency
corr_path = "data/analytics/gpa_correlations.csv"
corr_matrix.to_csv(corr_path, index=True)
print(f"Correlation matrix saved: {corr_path}")

# Display sorted correlations
print("\n=== Correlation with GPA ===")
print(corr_matrix["GPA"].sort_values(ascending=False))

# --- Step 4: Group analysis by categorical variables ---
group_vars = ["Gender", "ParentalSupport", "Extracurricular", "Sports", "Music", "Volunteering"]
group_summaries = {}

for var in group_vars:
    if var in df.columns:
        summary = df.groupby(var)["GPA"].mean().reset_index()
        group_summaries[var] = summary
        print(f"\n=== Mean GPA by {var} ===")
        print(summary)

# --- Step 5: Visualization ---
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Heatmap: GPA vs Student Environment Factors")
plt.tight_layout()
plt.savefig("data/analytics/gpa_correlation_heatmap.png", dpi=300)
plt.close()

# Scatter plot for strongest continuous factor (e.g., StudyTimeWeekly)
if "StudyTimeWeekly" in df.columns:
    sns.regplot(
        x="StudyTimeWeekly", 
        y="GPA", 
        data=df,
        scatter_kws={"alpha": 0.6, "s": 50},  
        line_kws={"color": "red", "linewidth": 2},  
        ci=None  
    )

    plt.title("Relationship between Study Time and GPA", fontsize=14)
    plt.xlabel("Weekly Study Time (hours)", fontsize=12)
    plt.ylabel("GPA", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("data/analytics/gpa_studytime_relationship.png", dpi=300)
    plt.close()

# --- Step 6: Save textual report ---
report_path = "data/analytics/analysis_report.txt"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("Analytic Verification of Curated Dataset\n")
    f.write("========================================\n\n")
    f.write("Correlation with GPA (Pearson):\n")
    f.write(str(corr_matrix["GPA"].sort_values(ascending=False)) + "\n\n")

    for var, summary in group_summaries.items():
        f.write(f"Mean GPA by {var}:\n")
        f.write(str(summary) + "\n\n")

    f.write("Visualization files:\n")
    f.write("- data/analytics/gpa_correlation_heatmap.png\n")
    f.write("- data/analytics/gpa_studytime_relationship.png\n")

print(f"Analytical summary saved: {report_path}")
print("GPA-environment relationships verified and visualized.")

write_provenance("Analysis Verification", "GPA correlation and group analysis completed.")