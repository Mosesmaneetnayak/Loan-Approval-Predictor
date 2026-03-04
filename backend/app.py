from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import io
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------
# LOAD MODEL
# ------------------
model = pickle.load(open("loan_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

MODEL_COLUMNS = [
    "Dependents",
    "Education",
    "Self_Employed",
    "Credit_History",
    "Property_Area",
    "Loan_Amount_Term",
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount"
]

# ------------------
# PREPROCESS INPUT
# ------------------
def preprocess(data):

    df = pd.DataFrame([data])

    # fix dependents
    df["Dependents"] = df["Dependents"].replace("3+", 3)

    # -------------------------
    # CONVERT RUPEES → THOUSANDS
    # -------------------------
    # user enters real rupees
    df["LoanAmount"] = df["LoanAmount"] / 1000

    # encode categorical columns
    for col in encoders:
        if col != "Loan_Status":
            df[col] = encoders[col].transform(df[col])

    return df[MODEL_COLUMNS]

# ------------------
# PREDICT API
# ------------------
@app.post("/predict")
def predict(data: dict):

    df_input = preprocess(data)

    pred = model.predict(df_input)[0]
    prob = model.predict_proba(df_input)[0][1]

    return {
        "prediction": "Approved" if pred == 1 else "Rejected",
        "probability": round(prob * 100, 2)
    }

# ------------------
# SCATTER PLOT API
# ------------------
@app.get("/plot")
def plot():

    df = pd.read_csv("train.csv")

    plt.figure()
    plt.scatter(df["ApplicantIncome"], df["LoanAmount"])
    plt.xlabel("Applicant Income")
    plt.ylabel("Loan Amount")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    image = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()

    return {"image": image}