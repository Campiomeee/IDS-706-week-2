import pandas as pd
from project.data import load_data, data_summary


def test_load_data(tmp_path):
    path = tmp_path / "test.csv"
    pd.DataFrame({"a": [1, 2], "b": [3, 4]}).to_csv(path, index=False)
    df = load_data(path)
    assert not df.empty
    assert list(df.columns) == ["a", "b"]


def test_data_summary():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    summary = data_summary(df)
    assert "shape" in summary
    assert summary["shape"] == (3, 2)
    assert "nulls" in summary
