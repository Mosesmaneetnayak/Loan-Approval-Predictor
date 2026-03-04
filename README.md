# 🚀 Loan Approval Prediction System
**Full-Stack Machine Learning Web Application**  

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/) 
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green?logo=fastapi)](https://fastapi.tiangolo.com/) 
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) 
[![GitHub Issues](https://img.shields.io/github/issues/your-username/loan-approval-system)](https://github.com/your-username/loan-approval-system/issues)

An end-to-end ML system predicting **loan approval status in real time**, with:

- REST API deployment
- Responsive frontend interface
- Data visualization
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

---

# 🧠 Overview

| Attribute | Details |
|-----------|---------|
| **Project Type** | Complete ML Deployment Pipeline |
| **Core Purpose** | Real-time Loan Approval Prediction |
| **Key Capabilities** | Model training, serialization, API deployment, frontend integration, dataset visualization |
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
| User (Browser) | Initiates request, inputs financial data |
| Frontend (HTML/CSS/JS) | Captures input, renders dynamic UI |
| Fetch API | Sends JSON data to backend |
| FastAPI Backend | Handles requests, routes to prediction endpoint |
| Preprocessing Pipeline | Encodes, scales, aligns features |
| Logistic Regression Model | Classifies loan approval |
| Prediction + Probability | Generates decision & confidence |
| JSON Response | Frontend dynamically updates UI |

---

# ✨ Features

| Feature | Description |
|---------|-------------|
| **Real-Time Loan Prediction** | Accepts user input and returns loan approval status + probability |
| **ML Pipeline** | Handles missing values, categorical encoding, feature alignment, classification, probability output |
| **Dataset Visualization** | Scatter plot (Applicant Income vs Loan Amount), Base64 API output |
| **Modern UI Experience** | Responsive design, dynamic styling, smooth animations, gradient interface |

---

# 🔬 Machine Learning Details

| Aspect | Details |
|--------|---------|
| **Algorithm** | Logistic Regression |
| **Max Iterations** | 2000 |
| **Outputs** | Approved / Rejected |
| **Input Features** | Dependents, Education, Self_Employed, Credit_History, Property_Area, Loan_Amount_Term, ApplicantIncome, CoapplicantIncome, LoanAmount |
| **Preprocessing** | "3+" Dependents normalization, missing value handling, Rupees → Thousands conversion, consistent feature ordering |

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
- Dynamically renders dataset visualization on frontend  

---

# 🛠 Installation & Setup

### Clone Repository
```bash
git clone https://github.com/your-username/loan-approval-system.git
cd loan-approval-system
```

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```
- Access backend at: `http://127.0.0.1:8000`

### Frontend Setup

**Option A – VS Code Live Server:**  
- Open `index.html` with Live Server  

**Option B – Python Server:**  
```bash
cd frontend
python -m http.server 5500
```
- Access frontend at: `http://127.0.0.1:5500`

### Model Training
```bash
cd backend
python train_model.py
```
- Trains Logistic Regression  
- Saves `loan_model.pkl` & `encoders.pkl`  

---

# 🧪 Experimental Model Lab

**Directory:** `/z_filess`  

| Content | Purpose |
|---------|---------|
| Alternate training pipeline | Experimentation |
| Accuracy evaluation | Model metrics |
| Feature experimentation | Test new features |
| Outlier threshold storage | Data quality control |
| Batch prediction outputs | Evaluate multiple samples |

- Supports iterative development prior to production  

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
loan-approval-system/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── requirements.txt
│   └── models/
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── scripts.js
└── z_filess/
    ├── alternate_pipeline.py
    └── batch_outputs/
```

---

# 📈 Screenshots (Optional)

- Include live frontend, API response, and dataset plots here for better documentation visuals.

---

# 📄 License

[MIT License](LICENSE)

---
