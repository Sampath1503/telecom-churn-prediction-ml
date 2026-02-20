import pandas as pd
from utils import load_data_from_sql

def get_latest_data():
    """
    Pull latest telecom customer data from SQL
    """
    df = load_data_from_sql()
    return df

if __name__ == "__main__":
    df = get_latest_data()
    print("Data pulled successfully:", df.shape)
