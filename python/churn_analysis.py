import pandas as pd
import matplotlib.pyplot as plt
import os

# File path
file_path = r"C:\temp\churn_sql_clean.csv"

# Screenshots folder
output_folder = r"C:\temp\screenshots"
os.makedirs(output_folder, exist_ok=True)

# Read CSV
df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nTotal rows:")
print(len(df))

print("\nColumns:")
print(df.columns.tolist())

# Make sure numeric columns are proper
df["tenure"] = pd.to_numeric(df["tenure"], errors="coerce")
df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce")

# 1. Churn Distribution
print("\nChurn Distribution:")
print(df["Churn"].value_counts())

plt.figure(figsize=(6, 4))
df["Churn"].value_counts().plot(kind="bar")
plt.title("Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(r"C:\temp\screenshots\churn_distribution.png")
plt.show()

# 2. Gender vs Churn
gender_churn = pd.crosstab(df["gender"], df["Churn"])
print("\nGender vs Churn:")
print(gender_churn)

gender_churn.plot(kind="bar", figsize=(6, 4))
plt.title("Gender vs Churn")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(r"C:\temp\screenshots\gender_vs_churn.png")
plt.show()

# 3. Contract vs Churn
contract_churn = pd.crosstab(df["Contract"], df["Churn"])
print("\nContract vs Churn:")
print(contract_churn)

contract_churn.plot(kind="bar", figsize=(7, 4))
plt.title("Contract vs Churn")
plt.xlabel("Contract Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(r"C:\temp\screenshots\contract_vs_churn.png")
plt.show()

# 4. Tenure Group vs Churn
def tenure_group(x):
    if x <= 9:
        return "0-9"
    elif x <= 19:
        return "10-19"
    else:
        return ">20"

df["tenure_group"] = df["tenure"].apply(tenure_group)

tenure_churn = pd.crosstab(df["tenure_group"], df["Churn"])
print("\nTenure Group vs Churn:")
print(tenure_churn)

tenure_churn.plot(kind="bar", figsize=(6, 4))
plt.title("Tenure Group vs Churn")
plt.xlabel("Tenure Group")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(r"C:\temp\screenshots\tenure_group_vs_churn.png")
plt.show()

# 5. Average Monthly Charges by Churn
avg_charges = df.groupby("Churn")["MonthlyCharges"].mean()
print("\nAverage Monthly Charges by Churn:")
print(avg_charges)

avg_charges.plot(kind="bar", figsize=(6, 4))
plt.title("Average Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")
plt.tight_layout()
plt.savefig(r"C:\temp\screenshots\avg_monthly_charges_by_churn.png")
plt.show()

print("\nAnalysis complete. Charts saved in C:\\temp\\screenshots")