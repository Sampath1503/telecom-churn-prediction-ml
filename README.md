
---

# 📊 Telecom Customer Churn Analysis & Business Insights (Power BI)

## 🔹 Project Overview

Customer churn is one of the most critical challenges in the telecom industry. Losing customers directly impacts revenue, especially when high-usage and high-value customers churn.

This project focuses on **analyzing customer churn behavior using descriptive and diagnostic analytics**, identifying key churn drivers, and translating insights into **actionable business recommendations** using **Power BI**.

The goal is **not prediction**, but to answer:

* *Who is churning?*
* *Why are they churning?*
* *What actions should the business take right now?*

---

## 🔹 Business Problem

Telecom companies face difficulty in:

* Identifying early signs of customer churn
* Understanding whether churn is driven by **usage, pricing, service issues, or plans**
* Prioritizing **high-risk, high-value customers** for retention

Without clear insights, retention strategies become reactive instead of proactive.

---

## 🔹 Dataset Description

**Source:** Telecom customer usage dataset
**Records:** 10,000 customers
**Target Variable:** `churn` (0 = Retained, 1 = Churned)

### Key Available Columns

* Customer behavior:
  `day_mins`, `eve_mins`, `night_mins`, `intl_mins`
* Charges:
  `day_charge`, `eve_charge`, `night_charge`, `intl_charge`
* Service experience:
  `customer_calls`
* Plan information:
  `intl_plan`, `voice_plan`
* Geography:
  `state`
* Account details:
  `account_length`

> Note: Revenue is not explicitly provided. **Charges are used as a proxy for customer value**, which is common in telecom analytics.

---

## 🔹 Tools & Technologies

* **SQL Server** – Data storage & querying
* **Power BI** – Data modeling, DAX, and dashboarding
* **DAX** – KPI and churn metrics
* **Data Analysis** – Descriptive & diagnostic analytics

---

## 🔹 Key Metrics (DAX Measures)

* **Total Customers**
* **Churned Customers**
* **Churn Rate %**
* **Average Customer Service Calls**
* **Average Usage (Minutes)**
* **Average Charges (Total & International)**

Example:

```DAX
Churn Rate % =
DIVIDE([Churned Customers], [Total Customers], 0)
```

---

## 🔹 Dashboard Structure

The analysis is organized into **three clear analytical pages**.

---

## 📄 Page 1 – Executive Overview

**Purpose:**
Provide a high-level snapshot of churn for leadership and stakeholders.

### Visuals Included

* KPI cards (Total Customers, Churn Rate, Churned Customers, Avg Calls)
* Customer base split (Retained vs Churned)
* Customer service calls vs churn
* International plan vs churn
* Churn rate by state

### Key Insights

* Overall churn rate is **14.14%**
* Customers with **international plans churn more**
* Churn varies significantly by **state**
* Customer service calls show a strong relationship with churn

---

## 📄 Page 2 – Usage, Charges & Service Behavior

**Purpose:**
Diagnose *why* customers churn by analyzing behavior patterns.

### Visuals Included

* Avg total usage by churn status
* Avg total charges by churn status
* Avg international charges by churn status
* Day vs Evening vs Night usage comparison
* Customer service calls vs churn rate

### Key Insights

* Churned customers often:

  * Use **more minutes**
  * Generate **higher charges**
* Churn is **not driven by low usage**
* Churn rate increases sharply after **4+ customer service calls**
* Service experience is a stronger churn driver than usage volume

---

## 📄 Page 3 – Business Insights & Recommendations

**Purpose:**
Translate analytics into **business decisions and actions**.

### Key Churn Drivers Identified

* High number of customer service calls
* High-usage and high-charge customers
* International calling plan users

### High-Risk Customer Profile

Customers most likely to churn:

* 4+ customer service calls
* High total usage (minutes)
* Higher average charges
* Active international calling plan

### Recommended Business Actions

1. **Improve Customer Support**

   * Trigger retention workflows after 3 service calls
   * Prioritize high-value customers

2. **Targeted Retention Offers**

   * Discounts for international plan users
   * Proactive outreach before churn occurs

3. **Early Warning System**

   * Monitor service calls, usage, and plans
   * Flag high-risk customers in CRM systems

---

## 🔹 Business Impact

This analysis helps telecom teams:

* Identify churn **before it happens**
* Focus retention efforts on **high-value customers**
* Reduce revenue loss caused by avoidable churn
* Align analytics with **real business decisions**

---

## 🔹 How This Project Fits a Real Company

This project mirrors real-world workflows:

* Analytics team → identifies churn drivers
* Business team → applies retention strategies
* ML team → later builds churn prediction models

This dashboard would typically be used **before** deploying predictive models.

---

## 🔹 Future Enhancements

* Integrate churn prediction models (Logistic Regression / XGBoost)
* Build customer segmentation based on behavior
* Automate refresh using live database connectors
* Add cohort-based churn analysis

---

## 🔹 Author

**Chintu**
Data Science & Analytics
Project: Telecom Customer Churn Analysis

---

### ✅ What this README does for you

* Makes your project **self-explanatory**
* Saves interviewers time
* Shows **business thinking**, not just Power BI skills
* Integrates cleanly with your **churn prediction ML project**

---

### Next logical steps (you choose)

1️⃣ Rewrite **resume project section**
2️⃣ Integrate this with **Churn Prediction ML project**
3️⃣ Prepare **interview explanations** using this dashboard

Say **“Next: Resume”** or **“Next: Integration with ML”** and we’ll move forward.
