# ======================================
# LOAN APPROVAL MODEL — TRAIN ONLY
# ======================================

import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ======================
# LOAD TRAIN DATA
# ======================
df = pd.read_csv("train.csv")

# ======================
# REMOVE UNUSED COLUMN
# ======================
df = df.drop(columns=["Loan_ID"])

# ======================
# HANDLE MISSING VALUES
# ======================
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# ======================
# FIX DEPENDENTS
# ======================
df["Dependents"] = df["Dependents"].replace("3+", 3).astype(int)

# ======================
# ENCODE CATEGORICAL
# ======================
encoders = {}

for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# ======================
# SPLIT FEATURES
# ======================
X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

# ======================
# TRAIN MODEL
# ======================
model = LogisticRegression(max_iter=500)
model.fit(X, y)

# ======================
# TRAIN ACCURACY
# ======================
pred = model.predict(X)
acc = accuracy_score(y, pred)

print("Training Accuracy:", round(acc * 100, 2), "%")

# ======================
# SAVE MODEL (OPTIONAL)
# ======================
pickle.dump(model, open("loan_model.pkl", "wb"))
pickle.dump(encoders, open("encoders.pkl", "wb"))

# ======================
# SCATTER PLOT
# ======================
plt.figure()

plt.scatter(
    X["ApplicantIncome"],
    X["LoanAmount"],
    c=pred
)

plt.xlabel("Applicant Income")
plt.ylabel("Loan Amount")
plt.title("Loan Approval Prediction")

plt.show()