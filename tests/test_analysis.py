import pandas as pd
from project.analysis import average_salary_by_role, count_high_salary


def test_average_salary_by_role():
    df = pd.DataFrame({
        "job_title": ["A", "A", "B"],
        "salary_usd": [100, 200, 300]
    })
    avg = average_salary_by_role(df)
    assert "salary_usd" in avg.columns
    assert avg.loc[avg["job_title"] == "A", "salary_usd"].iloc[0] == 150


def test_count_high_salary():
    df = pd.DataFrame({"salary_usd": [50000, 200000, 120000]})
    count = count_high_salary(df, 100000)
    assert count == 2
