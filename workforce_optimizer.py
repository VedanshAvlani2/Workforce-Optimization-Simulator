import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------
# 1. Load Dataset
# ------------------------
df = pd.read_csv("employee_workforce.csv")  

# ------------------------
# 2. Calculate Assigned Weekly Hours
# ------------------------
schedule_cols = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
df[schedule_cols] = df[schedule_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

df["Working_Days"] = df[schedule_cols].sum(axis=1)
df["Assigned_Hours"] = df.apply(
    lambda row: 0 if row["Working_Days"] == 0 
    else (row["Work_Hours_Per_Week"] / row["Working_Days"]) * row[schedule_cols].sum(), axis=1
)

# ------------------------
# 3. Utilization Metrics
# ------------------------
df["Utilization_Ratio"] = df["Assigned_Hours"] / df["Work_Hours_Per_Week"]
df["Underutilized"] = df["Utilization_Ratio"] < 0.5
df["Overutilized"] = df["Utilization_Ratio"] > 1.1

# ------------------------
# 4. Summary
# ------------------------
print("📊 Optimization Summary")
print("Total Employees         :", len(df))
print("Avg Assigned Hours      :", round(df["Assigned_Hours"].mean(), 2))
print("Underutilized Workers   :", df["Underutilized"].sum())
print("Overutilized Workers    :", df["Overutilized"].sum())
print("Avg Utilization Ratio   :", round(df["Utilization_Ratio"].mean(), 2))

# ------------------------
# 5. Visualizations
# ------------------------
plt.figure(figsize=(8, 4))
sns.histplot(df["Assigned_Hours"], kde=False, bins=10, color="skyblue")
plt.title("Distribution of Assigned Weekly Hours")
plt.xlabel("Assigned Hours")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Assigned_Hours"])
plt.title("Boxplot: Weekly Workload Distribution")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
sns.countplot(data=df, x="Group", hue="Overutilized")
plt.title("Overutilization by Group")
plt.tight_layout()
plt.show()

# ------------------------
# 6. Save Updated Dataset
# ------------------------
df.to_csv("workforce_optimized.csv", index=False)
print("✅ Saved updated dataset as workforce_optimized.csv")
