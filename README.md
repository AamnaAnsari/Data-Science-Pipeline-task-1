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
