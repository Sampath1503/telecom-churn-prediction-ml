# automation/config.py

BASE_PATH = "automation"

MODEL_PATH = f"{BASE_PATH}/models/churn_pipeline.pkl"
OUTPUT_PATH = f"{BASE_PATH}/outputs/churn_risk_output.csv"
LOG_PATH = f"{BASE_PATH}/logs/automation.log"

# Data source (CSV snapshot for automation v2)
CSV_PATH = "data/telecom_churn_snapshot.csv"

# Risk thresholds
LOW_RISK_THRESHOLD = 0.3
HIGH_RISK_THRESHOLD = 0.7

LOG_LEVEL = "INFO"

