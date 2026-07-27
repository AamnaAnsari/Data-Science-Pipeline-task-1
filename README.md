# Data Science Pipeline - Alphatron Technologies

This repository contains the end-to-end Data Science and Machine Learning pipeline developed during the AI Engineering internship at Alphatron Technologies. The project strictly follows industry standards, including Object-Oriented Programming (OOP), modular architecture, and robust error handling.

## 🚀 Features Implemented
* **Modular Architecture:** Clean separation of source code (`src/`), exploratory notebooks (`notebooks/`), and datasets (`data/`).
* **Professional Data Ingestion:** A `DataLoader` class equipped to handle CSV and Excel files with automated summary generation.
* **Production-Grade Logging:** Standard `print` statements are replaced with Python's `logging` module for better state tracking.
* **Strict Data Privacy:** Adherence to internal IP policies by completely isolating raw and processed data from version control.

## 📂 Project Structure
```text
├── data/
│   ├── processed/    # Cleaned data (Git-ignored)
│   └── raw/          # Original datasets (Git-ignored)
├── notebooks/        # Jupyter notebooks for EDA 
├── src/              # Source code modules
│   └── data_loader.py
├── .gitignore        # Security rules to prevent data leaks
├── README.md         # Project documentation
└── test_run.py       # Pipeline execution script

```

## 🚀 Current Progress & Milestones

### Phase 1: Setup & Initialization ✅
* **Environment:** Configured the virtual environment and effectively managed dependencies.
* **Data Ingestion:** Implemented a modular `DataLoader` class for robust data ingestion.

### Phase 2: Data Cleaning & Imputation ✅
* **Missing Data:** Handled missing values (`NaN`) across multiple columns to ensure data integrity.
* **Imputation Strategy:** Applied median imputation for `Age` and mean imputation for `LoyaltyScore`.

### Phase 3: Exploratory Data Analysis (EDA) ✅
* **Statistical Analysis:** Performed comprehensive univariate and bivariate analysis.
* **Data Visualization:** Generated distribution and scatter plots (e.g., Age vs. TotalPurchases by City) to uncover patterns.
* **Data Persistence:** Persisted the cleaned dataset to the `data/processed/` directory for downstream tasks.

### Phase 4: Feature Engineering ⏳ *(In Progress)*
* **Categorical Encoding:** Applying encoding techniques for text-based variables.
* **Numerical Scaling:** Implementing scaling and transformation for machine learning readiness.
