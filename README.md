
---

# 📊 Telecom Customer Churn Analytics & Prediction System

<p align="center">
End-to-end ML pipeline with automated batch scoring and Power BI business intelligence integration.
</p>

---

## 🚀 Project Overview

This system delivers a production-style churn analytics workflow:

* SQL-based data sourcing
* Feature engineering & imbalance handling
* XGBoost-based predictive modeling
* Automated batch inference pipeline
* Risk segmentation logic
* Power BI dashboard integration

The focus is not just prediction — but operational decision support.

---

## 🎯 Business Problem

Telecom providers face revenue leakage due to customer churn.

This system enables:

* Identification of high-value at-risk customers
* Behavioral churn driver analysis
* Risk-based segmentation for retention campaigns
* Automated daily prediction workflow

---

## 🏗️ System Architecture

```
SQL Server (SSMS)
        ↓
CSV Snapshot
        ↓
Model Training (Colab)
        ↓
churn_pipeline.pkl
        ↓
Batch Inference (Python)
        ↓
churn_risk_output.csv
        ↓
Power BI Dashboard
```

Automation: Windows Task Scheduler + structured logging.

---

# 📈 Power BI Dashboard Preview

---

### 📊 Executive Overview

<p align="center">
  <img src="assets/01_executive_churn_overview.png" width="900">
</p>

---

### 🔍 Churn Driver Analysis

<p align="center">
  <img src="assets/02_churn_driver_analysis.png" width="900">
</p>

---

### 💼 Business Insights & Retention Strategy

<p align="center">
  <img src="assets/03_Business_Insights_And_Retention_Strategy.png" width="900">
</p>

---

### 🚦 Risk Monitoring & Model Output

<p align="center">
  <img src="assets/04_Churn_Risk_Monitoring_And_Model_Output.png" width="900">
</p>

---

## 📂 Dataset Overview

* ~10,000 telecom customers
* Binary target: Churn (Yes / No)

Key features:

* Usage metrics (day, evening, night, international)
* Billing charges
* Service calls
* Account tenure
* Plan subscriptions

---

## ⚙️ Feature Engineering

Engineered features include:

* Total usage aggregation
* Total charge aggregation
* Charge-per-minute ratio
* Service call binning
* International usage indicator
* Behavioral risk segmentation

Goal: Improve minority class signal detection.

---

## 🤖 Machine Learning Pipeline

Model: **XGBoost Classifier**

Techniques used:

* SMOTETomek for class imbalance
* RandomizedSearchCV
* Cross-validation
* Precision / Recall / F1 evaluation

Output:

* Churn probability (0–1)
* Risk segment label

---

## 📊 Model Performance

| Metric            | Value |
| ----------------- | ----- |
| Accuracy          | ~98%  |
| Recall (Churn)    | ~87%  |
| Precision (Churn) | ~98%  |

Confusion Matrix:

```
[[856   3]
 [ 19 122]]
```

Primary focus: Maximize churn recall without sacrificing overall precision.

---

## 🚦 Risk Segmentation Logic

| Risk Level  | Probability | Business Action           |
| ----------- | ----------- | ------------------------- |
| Low Risk    | < 0.30      | Monitor                   |
| Medium Risk | 0.30 – 0.70 | Proactive outreach        |
| High Risk   | > 0.70      | Immediate retention offer |

Transforms ML output into operational strategy.

---

## ⏱️ Automation Layer

Batch pipeline:

* Load trained model
* Ingest latest snapshot
* Generate probabilities
* Apply segmentation logic
* Export business-ready CSV
* Log execution status

Scheduled daily via Windows Task Scheduler.

---

## 📁 Project Structure

```
telecom-churn-portfolio/
│
├── assets/
├── dashboards/
├── notebooks/
├── src/
│   ├── train_churn_model.py
│   ├── predict_churn.py
│   ├── utils.py
│
└── README.md
```

---

## ▶️ How to Run

1. Train model (Colab) → download `churn_pipeline.pkl`
2. Place inside `models/`
3. Run:

   ```
   python predict_churn.py
   ```
4. Refresh Power BI dashboard

---

## 💼 Business Impact

* Identifies revenue exposure
* Enables targeted retention campaigns
* Reduces manual reporting effort
* Bridges ML with operational BI

---

## 📊 Project Presentation

Comprehensive slide deck covering data analysis, predictive modeling, automation workflow, and business strategy.

📄 [View Full Presentation](presentations/telecom_churn_analytics_prediction.pdf)

---

## 🔮 Future Enhancements

* Drift monitoring
* Automated retraining
* Cloud-based batch scoring
* Real-time API scoring
* A/B testing integration

---

