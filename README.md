# 🚀 Loan Approval Prediction System
**Full-Stack Machine Learning Web Application**

An end-to-end ML system predicting loan approval status in real time using a deployed REST API and a responsive frontend interface.

---

# 🧠 Overview

- **Project Type:** Complete Machine Learning Deployment Pipeline  
- **Core Purpose:** Real-time Loan Approval Prediction  

### 🚀 Key Capabilities

- Train classification models for loan approval  
- Serialize models and encoders for deployment  
- Serve predictions via high-performance API  
- Integrate with dynamic frontend interface  
- Visualize dataset insights  

### 🛠️ Technology Stack

- **Backend:** FastAPI  
- **ML & Data Processing:** scikit-learn, pandas  
- **Frontend:** HTML, CSS, JavaScript  

---

# 🏗 System Architecture

### 🔄 End-to-End Flow

1. **User (Browser)** – Initiates interaction through the web interface  
2. **Frontend (HTML/CSS/JS)** – Captures input & renders UI  
3. **Fetch API Requests** – Sends user data in JSON format to backend  
4. **FastAPI Backend** – Routes requests to prediction endpoint  
5. **Preprocessing Pipeline** – Encodes and scales features for model input  
6. **Logistic Regression Model** – Performs classification  
7. **Prediction + Probability** – Computes approval decision and confidence  
8. **JSON Response → Frontend Rendering** – Dynamically updates UI  

---

# ✨ Features

### 🔮 Real-Time Loan Prediction

- Accepts user financial details  
- Returns:
  - **Loan Approval Status**  
  - **Approval Probability (%)**  

### 🎯 Machine Learning Pipeline

- Handles missing values  
- Categorical encoding with `LabelEncoder`  
- Feature alignment for consistency  
- Logistic Regression classification  
- Probability-based output  

### 📊 Dataset Visualization

- Scatter plot: Applicant Income vs Loan Amount  
- Delivered via Base64 encoded image API for frontend rendering  

### 🎨 Modern UI Experience

- Responsive layout  
- Dynamic success/error styling  
- Loading states with smooth animations  
- Clean, gradient-based interface  

---

# 🔬 Machine Learning Details

### 🧩 Model

- **Algorithm:** Logistic Regression  
- **Max Iterations:** 2000  
- **Outputs:** Approved / Rejected  

### 📝 Input Features

- Dependents, Education, Self_Employed, Credit_History  
- Property_Area, Loan_Amount_Term  
- ApplicantIncome, CoapplicantIncome, LoanAmount  

### ⚙️ Preprocessing Highlights

- Normalize "3+" dependents  
- Handle missing values  
- Convert Rupees → Thousands during inference  
- Ensure consistent feature ordering before prediction  

---

# 🌐 API Documentation

### 🔹 POST `/predict`

**Request Body**
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

---

### 🔹 GET `/plot`

**Response**
```json
{
  "image": "<base64_encoded_png>"
}
```

- Used by frontend to render dataset visualization dynamically.  

---

# 🛠 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/loan-approval-system.git
cd loan-approval-system
```

### 2️⃣ Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

- Backend runs at: `http://127.0.0.1:8000`  

### 3️⃣ Frontend Setup

**Option A – VS Code Live Server:**  
- Right click `index.html` → Open with Live Server  

**Option B – Python Server:**
```bash
cd frontend
python -m http.server 5500
```
- Open: `http://127.0.0.1:5500`  

### 📈 Model Training

To retrain the model:
```bash
cd backend
python train_model.py
```

- Trains Logistic Regression  
- Saves `loan_model.pkl` & `encoders.pkl`  

---

# 🧪 Experimental Model Lab

### 🔹 /z_filess Directory

- Alternate training pipeline  
- Accuracy evaluation  
- Feature experimentation  
- Outlier threshold storage  
- Batch prediction outputs  

**Purpose:** Supports iterative model development before production deployment  

---

# ⚡ Final Statement

This project demonstrates:

- End-to-end ML lifecycle  
- API-based model deployment  
- Frontend-backend integration  
- Production-style architecture  
- Real-world financial prediction capability  

---
