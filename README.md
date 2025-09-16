# 1. IDS-706-week-2-Analysis

## 🚀  This project will:
    
    Use a dev container, Makefile, and GitHub Actions
    
    Use data set of Global AI Job Market & Salary Trends 2025 (Source: https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025?select=ai_job_dataset.csv)
    
    Do an analysis on the data set with the following steps:
        1.Import the Dataset
        2.Inspect the Data
        3.Display the first few rows using .head() to get a quick overview.
        4.Use .info() and .describe() to understand data types and summary statistics.
        5.Check for missing values and duplicates.
        6.Basic Filtering and Grouping of high salary group of people and average of different roles.
        7.Apply K-mean to cluster people with different levels of salaries.
        8.Apply Linear regression to find the relationship between the colunns salary_usc and years_experience.
        9.Visualize the results of both models with different plots.


Run the requirements.txt which contains the following packages:
create a requirements.txt file with:
pandas
numpy
matplotlib
yfinance
pytest
flake8
seaborn
jupyter
scipy

The Second Part of the project: Pytest and container.
# 2. IDS 706 Week 2 Project – Reproducibility & Testing

This repository contains a **data analysis pipeline** that has been made reproducible and testable using **unit tests** and **containerization**.  

---

## 🚀 Features
- **Modular Codebase**: Split into `data`, `preprocess`, `analysis`, and `model` modules.  
- **Unit & System Tests**: Cover data loading, cleaning, grouping, preprocessing, and machine learning model behavior.  
- **Containerized Environment**: Runs consistently with either **Docker** or **Dev Container** (VS Code).  
- **CI-Ready**: Easily extendable to GitHub Actions or other CI/CD tools.  

---

## 📂 Repository Structure!
project/
init.py
data.py
preprocess.py
analysis.py
model.py
tests/
test_data.py
test_preprocess.py
test_analysis.py
test_model.py//
requirements.txt
Dockerfile
README.md
IDS_706_Week2_Analysis.ipynb

test reulst:

Run with docker:

![](../../../../../var/folders/xr/cf3s83ls3ln7173fhjgq50_m0000gn/T/TemporaryItems/NSIRD_screencaptureui_xIc0VO/Screenshot 2025-09-15 at 10.08.04 pm.png)

Run locally:

![](../../../../../var/folders/xr/cf3s83ls3ln7173fhjgq50_m0000gn/T/TemporaryItems/NSIRD_screencaptureui_cv49Wy/Screenshot 2025-09-15 at 9.54.55 pm.png)