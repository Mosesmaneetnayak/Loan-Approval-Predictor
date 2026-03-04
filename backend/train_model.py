# ==================================
# SIMPLE LOAN MODEL (FINAL FIXED)
# ==================================

import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

# ------------------
# LOAD DATA
# ------------------
df = pd.read_csv("train.csv")

# keep only needed columns
df = df[[
    "Dependents",
    "Education",
    "Self_Employed",
    "Credit_History",
    "Property_Area",
    "Loan_Amount_Term",
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Status"
]]

# ------------------
# CLEAN DEPENDENTS
# ------------------
df["Dependents"] = df["Dependents"].replace("3+", "3")
df["Dependents"] = df["Dependents"].astype(str)   # ⭐ FIX

# ------------------
# HANDLE MISSING VALUES
# ------------------
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# ------------------
# ENCODE CATEGORICAL
# ------------------
encoders = {}

for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))  # ⭐ FIX
    encoders[col] = le

# ------------------
# TRAIN MODEL
# ------------------
X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

model = LogisticRegression(max_iter=2000)
model.fit(X, y)

print("✅ Model trained successfully")

# ------------------
# SAVE MODEL
# ------------------
pickle.dump(model, open("loan_model.pkl", "wb"))
pickle.dump(encoders, open("encoders.pkl", "wb"))

# ------------------
# SCATTER PLOT
# ------------------
plt.figure()
plt.scatter(X["ApplicantIncome"], X["LoanAmount"])
plt.xlabel("Applicant Income")
plt.ylabel("Loan Amount")
plt.title("Loan Dataset Scatter Plot")
plt.show()