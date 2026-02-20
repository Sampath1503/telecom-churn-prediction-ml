from utils import load_data_from_csv, feature_engineering
import joblib
import pandas as pd

# -----------------------------
# 1. Load data
# -----------------------------
df = load_data_from_csv("data/telecom_churn_snapshot.csv")
df = feature_engineering(df)

# -----------------------------
# 2. Prepare features
# -----------------------------
X = df.drop(columns=['churn'])

# -----------------------------
# 3. Load trained model
# -----------------------------
model = joblib.load("churn_pipeline.pkl")

# -----------------------------
# 4. Predict churn probability
# -----------------------------
df['churn_probability'] = model.predict_proba(X)[:, 1]

# -----------------------------
# 5. Risk segmentation
# -----------------------------
def risk_bucket(prob):
    if prob >= 0.7:
        return "High Risk"
    elif prob >= 0.4:
        return "Medium Risk"
    else:
        return "Low Risk"

df['risk_segment'] = df['churn_probability'].apply(risk_bucket)

# -----------------------------
# 6. Save output for business / Power BI
# -----------------------------
output_path = "churn_risk_output.csv"

df[
    [
        'state',
        'customer_calls',
        'total_charge',
        'churn_probability',
        'risk_segment'
    ]
].to_csv(output_path, index=False)

print(f"✅ File created successfully: {output_path}")