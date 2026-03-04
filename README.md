# 🚀 Loan Approval Prediction System
**Full-Stack Machine Learning Web Application**  

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/) 
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green?logo=fastapi)](https://fastapi.tiangolo.com/) 
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) 
[![GitHub Issues](https://img.shields.io/github/issues/your-username/loan-approval-system)](https://github.com/your-username/loan-approval-system/issues)

An end-to-end ML system that predicts **loan approval status in real-time**, featuring:

- REST API deployment with FastAPI  
- Responsive frontend interface  
- Dataset visualization  
- Production-style architecture  

---

## 📌 Table of Contents

1. [Overview](#🧠-overview)  
2. [System Architecture](#🏗-system-architecture)  
3. [Features](#✨-features)  
4. [Machine Learning Details](#🔬-machine-learning-details)  
5. [API Documentation](#🌐-api-documentation)  
6. [Installation & Setup](#🛠-installation--setup)  
7. [Experimental Model Lab](#🧪-experimental-model-lab)  
8. [Final Statement](#⚡-final-statement)  
9. [Repository Structure](#📂-repository-structure)  

---

# 🧠 Overview

| Attribute | Details |
|-----------|---------|
| **Project Type** | Complete ML Deployment Pipeline |
| **Purpose** | Real-time Loan Approval Prediction |
| **Capabilities** | Model training, serialization, API deployment, frontend integration, dataset visualization |
| **Tech Stack** | FastAPI, scikit-learn, pandas, HTML/CSS/JS |

---

# 🏗 System Architecture

**End-to-End Flow:**  

```text
User → Frontend → Fetch API → FastAPI Backend → Preprocessing → Logistic Regression → Prediction → JSON Response → Frontend Rendering
```

**Stepwise Details:**

| Component | Role |
|-----------|------|
| User (Browser) | Inputs loan application data |
| Frontend (HTML/CSS/JS) | Captures input, renders dynamic UI |
| Fetch API | Sends data as JSON to backend |
| FastAPI Backend | Handles `/predict` and `/plot` endpoints |
| Preprocessing | Encodes categorical data, scales features |
| Logistic Regression Model | Predicts loan approval |
| Prediction + Probability | Returns approval decision & probability |
| JSON Response | Frontend dynamically updates UI with results |

---

# ✨ Features

| Feature | Description |
|---------|-------------|
| **Real-Time Loan Prediction** | Accepts user data, returns loan approval and probability |
| **ML Pipeline** | Handles missing values, categorical encoding, feature alignment |
| **Dataset Visualization** | Scatter plot of Applicant Income vs Loan Amount (Base64 API output) |
| **Modern UI** | Responsive, gradient-based interface, dynamic cards, animations |

---

# 🔬 Machine Learning Details

| Aspect | Details |
|--------|---------|
| **Algorithm** | Logistic Regression |
| **Max Iterations** | 2000 |
| **Outputs** | Approved / Rejected |
| **Input Features** | Dependents, Education, Self_Employed, Credit_History, Property_Area, Loan_Amount_Term, ApplicantIncome, CoapplicantIncome, LoanAmount |
| **Preprocessing** | Fix Dependents (`3+ → 3`), handle missing values, encode categoricals, scale LoanAmount |

---

# 🌐 API Documentation

### POST `/predict`

**Request**
```json
{
  "Dependents": "1",
  "Education": "Graduate",
  "Self_Employed": "No",
  "Credit_History": 1,
  "Property_Area": "Urban",
  "Loan_Amount_Term": 360,
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 2000,
  "LoanAmount": 150000
}
```

**Response**
```json
{
  "prediction": "Approved",
  "probability": 87.43
}
```

### GET `/plot`

**Response**
```json
{
  "image": "<base64_encoded_png>"
}
```

- Dynamically renders dataset scatter plot on frontend.

---

# 🛠 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/loan-approval-system.git
cd Loan-Approval-System
```

### 2️⃣ Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```
- Backend API runs at `http://127.0.0.1:8000`

### 3️⃣ Frontend Setup

**Option A – VS Code Live Server**  
- Open `index.html` with Live Server.

**Option B – Python HTTP Server**
```bash
cd frontend
python -m http.server 5500
```
- Access frontend at `http://127.0.0.1:5500`

### 4️⃣ Model Training
```bash
cd backend
python train_model.py
```
- Trains Logistic Regression  
- Saves `loan_model.pkl` & `encoders.pkl`

---

# 🧪 Experimental Model Lab

**Directory:** `/z_filess/filess`  

| File | Purpose |
|------|---------|
| LP_2.py | Alternate training script for experiments |
| loan_predictions.csv | Batch prediction results |
| loan_model.pkl | Experimental model |
| encoders.pkl | Experimental encoders |
| outliers.pkl | Outlier thresholds for feature preprocessing |

- Supports iterative development prior to production deployment.

---

# ⚡ Final Statement

This project demonstrates:

- End-to-end ML lifecycle  
- API-based model deployment  
- Frontend-backend integration  
- Production-style architecture  
- Real-world financial prediction capability  

---

# 📂 Repository Structure

```
Loan-Approval-System/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── loan_model.pkl
│   ├── encoders.pkl
│   ├── train.csv
│   └── test.csv
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── z_filess/
    └── filess/
        ├── LP_2.py
        ├── loan_predictions.csv
        ├── loan_model.pkl
        ├── encoders.pkl
        └── outliers.pkl
```

---

# 📈 Screenshots (Optional)

- Frontend UI view  
- Prediction result cards  
- Scatter plot visualization  

---

# 📄 License

[MIT License](LICENSE)

---
