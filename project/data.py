import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load dataset from CSV file."""
    return pd.read_csv(path)


def data_summary(df: pd.DataFrame) -> dict:
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "nulls": df.isnull().sum().to_dict(),
        "description": df.describe(include="all").to_dict(),
    }
