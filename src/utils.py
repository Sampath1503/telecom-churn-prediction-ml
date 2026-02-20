import pandas as pd

EXPECTED_COLUMNS = [
    'column1','state','area_code','account_length','voice_plan',
    'voice_messages','intl_plan','intl_mins','intl_calls','intl_charge',
    'day_mins','day_calls','day_charge','eve_mins','eve_calls',
    'eve_charge','night_mins','night_calls','night_charge',
    'customer_calls','churn'
]

def load_data_from_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, header=None)

    if df.shape[1] != len(EXPECTED_COLUMNS):
        raise ValueError("Schema mismatch")

    df.columns = EXPECTED_COLUMNS
    df.drop(columns=['column1'], inplace=True)
    df['churn'] = df['churn'].astype(int)
    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df['total_charge'] = (
        df['day_charge'] +
        df['eve_charge'] +
        df['night_charge'] +
        df['intl_charge']
    )

    df['total_mins'] = (
        df['day_mins'] +
        df['eve_mins'] +
        df['night_mins'] +
        df['intl_mins']
    )

    df['total_calls'] = (
        df['day_calls'] +
        df['eve_calls'] +
        df['night_calls'] +
        df['intl_calls']
    )

    def service_call_bin(calls):
        if calls == 0:
            return '0_calls'
        elif calls <= 3:
            return '1-3_calls'
        else:
            return '4+_calls'

    df['service_call_bin'] = df['customer_calls'].apply(service_call_bin)

    df['pay_as_you_go_intl'] = (
        (df['intl_plan'] == 0) & (df['intl_mins'] > 0)
    ).astype(int)

    return df
