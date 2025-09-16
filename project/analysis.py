import pandas as pd

def average_salary_by_role(df: pd.DataFrame) -> pd.DataFrame:
    # average salary
    return df.groupby("job_title")["salary_usd"].mean().reset_index()

def count_high_salary(df: pd.DataFrame, threshold: int = 100000) -> int:
    # Extremely high salary
    return df[df["salary_usd"] > threshold].shape[0]