import pandas as pd
import numpy as np
from project.preprocess import drop_missing, filter_high_salary, scale_features


def test_drop_missing():
    df = pd.DataFrame({"a": [1, None, 3]})
    result = drop_missing(df)
    assert result.shape[0] == 2


def test_filter_high_salary():
    df = pd.DataFrame({"salary_usd": [50000, 150000]})
    result = filter_high_salary(df, 100000)
    assert all(result["salary_usd"] > 100000)


def test_scale_features():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [2, 4, 6]})
    scaled, scaler = scale_features(df, ["x", "y"])
    assert scaled.shape == (3, 2)
    assert np.allclose(scaled.mean(axis=0).round(), [0, 0])
