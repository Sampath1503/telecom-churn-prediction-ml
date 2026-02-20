---

## 📊 Telecom Customer Churn Analysis & Prediction

### 🔍 Problem Statement

Telecom companies lose significant revenue when customers churn.
The challenge is not just predicting churn, but **identifying high-risk customers early and enabling actionable retention strategies**.

---

### 🧠 Solution Overview

This project delivers an **end-to-end churn analytics and prediction system**, combining:

* SQL-based data sourcing
* Feature-rich churn modeling
* Cloud-based ML training
* Automated churn risk segmentation
* Business-ready outputs for Power BI dashboards

---

### 🏗️ Architecture

```
SQL Server → CSV Snapshot → ML Training (Colab)
                      ↓
               Trained Model (.pkl)
                      ↓
             Local Inference Pipeline
                      ↓
           Power BI / Business Actions
```

---

### 🛠️ Tools & Technologies

* **SQL Server (SSMS)** – Source of truth
* **Python (Pandas, scikit-learn, XGBoost)** – ML pipeline
* **imbalanced-learn (SMOTETomek)** – Class imbalance handling
* **Google Colab** – Model training
* **Power BI** – Visualization & insights

---

### ⚙️ Feature Engineering Highlights

* Total usage & charge aggregation
* Service call behavior binning
* International usage pain indicator
* Value-based customer signals

---

### 🤖 Machine Learning

* Model: **XGBoost Classifier**
* Hyperparameter tuning with **RandomizedSearchCV**
* Class imbalance handled using **SMOTETomek**
* Output: **Churn probability (0–1)**

---

### 🚦 Risk Segmentation

Churn probabilities are converted into actionable segments:

| Risk Level  | Action                     |
| ----------- | -------------------------- |
| Low Risk    | Monitor                    |
| Medium Risk | Proactive outreach         |
| High Risk   | Immediate retention offers |

---

### 📈 Business Impact

* Identifies **high-value customers at risk**
* Enables **targeted retention strategies**
* Converts ML predictions into **business decisions**

---

### 📂 Outputs

* `churn_pipeline.pkl` – Trained ML model
* `churn_risk_output.csv` – Business-ready churn risk data
* Power BI dashboard for stakeholder insights

---

## 🚀 How to Run

1. Train model in Colab
2. Download `churn_pipeline.pkl`
3. Run:

```bash
python predict_churn.py
```

4. Load output CSV into Power BI

---

---
