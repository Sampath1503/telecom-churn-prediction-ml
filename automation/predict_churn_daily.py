import logging
from config import LOG_PATH, LOG_LEVEL
import sys
import os
import joblib
import pandas as pd

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import load_data_from_csv, feature_engineering
from config import MODEL_PATH, OUTPUT_PATH, CSV_PATH, LOW_RISK_THRESHOLD, HIGH_RISK_THRESHOLD


logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def assign_risk(prob):
    if prob >= HIGH_RISK_THRESHOLD:
        return "High Risk"
    elif prob >= LOW_RISK_THRESHOLD:
        return "Medium Risk"
    else:
        return "Low Risk"


def run_daily_prediction():
    try:
        logging.info("Daily churn prediction job started.")

        model = joblib.load(MODEL_PATH)
        logging.info("Model loaded successfully.")

        df = load_data_from_csv(CSV_PATH)
        logging.info(f"Data loaded: {df.shape}")

        if df.empty:
            logging.warning("Input data is empty. Job aborted.")
            return

        df = feature_engineering(df)

        df["churn_probability"] = model.predict_proba(df)[:, 1]
        df["risk_segment"] = df["churn_probability"].apply(assign_risk)

        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        df.to_csv(OUTPUT_PATH, index=False)

        logging.info("Churn risk output generated successfully.")
        logging.info("Daily churn prediction job completed.")

    except Exception as e:
        logging.error(f"Automation job failed: {e}", exc_info=True)



if __name__ == "__main__":
    run_daily_prediction()