import pandas as pd
from sklearn.preprocessing import StandardScaler


def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def filter_high_salary(df: pd.DataFrame, min_salary: int = 100000):
    return df[df["salary_usd"] > min_salary]


def scale_features(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[cols])
    return scaled, scaler
