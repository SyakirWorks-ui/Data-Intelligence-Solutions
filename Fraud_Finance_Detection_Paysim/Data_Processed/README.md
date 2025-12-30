# Processed Data Directory

This directory contains the refined datasets used for training and testing the Financial Fraud Detection model. Due to the original PaySim dataset exceeding GitHub's file size limits, these processed samples are provided to ensure the project remains reproducible.

## 📊 Dataset Specifications
The following files have been pre-processed to handle class imbalance and feature engineering:

* **`balanced_sample_20k.csv`**: A balanced subset of 20,000 transactions. This file was created using undersampling techniques to provide an equal distribution between fraudulent and legitimate classes, preventing model bias.
* **`final_features_20k.csv`**: This file contains the finalized feature set after rigorous feature engineering, scaling, and encoding. It is ready for immediate use in machine learning algorithms.

## 🛠 Pre-processing Workflow
The datasets in this folder were generated through the following pipeline located in the `notebooks/` directory:
1.  **Data Cleaning**: Removal of duplicates and handling missing values.
2.  **Feature Engineering**: Creation of new features to capture transaction patterns.
3.  **Resampling**: Balancing the target class for optimal model performance.

> **Note**: The full raw dataset can be accessed via [Kaggle - PaySim Financial Fraud Detection](https://www.kaggle.com/datasets/ealaxi/paysim1).
