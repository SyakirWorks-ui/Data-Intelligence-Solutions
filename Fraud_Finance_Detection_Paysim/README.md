# Financial Fraud Detection using PaySim Dataset

This repository contains a comprehensive Machine Learning pipeline for detecting fraudulent financial transactions. Using the PaySim synthetic dataset, this project demonstrates end-to-end data processing, feature engineering, and model deployment.

## 📌 Project Overview
The goal of this project is to identify fraudulent activities in mobile money transactions. Given the highly imbalanced nature of financial data, this project focuses on robust feature engineering and sampling techniques to ensure high detection accuracy for fraud cases.

## 📂 Repository Structure
The project is organized into specific directories for better maintainability:

* **`Data_Processed/`**: Contains balanced and engineered dataset samples ready for modeling.
* **`models/`**: Stores the trained Random Forest model (`.pkl` format).
* **`notebooks/`**: Includes the core Python scripts for Data Cleaning, EDA, and Model Training.
* **`src/`**: Contains the Streamlit application scripts for real-time fraud prediction.
* **`visualizations/`**: Stores key insights and charts generated during the Exploratory Data Analysis (EDA).

## 🚀 Key Features
* **Data Cleaning & Balancing**: Handled extreme class imbalance using undersampling techniques to improve model sensitivity.
* **Feature Engineering**: Created transaction-based features to better capture suspicious behavior.
* **Machine Learning Model**: Utilized a Random Forest Classifier to achieve high precision and recall.
* **Interactive Web App**: Developed a Streamlit interface for users to test transaction data against the model.

## 📊 Results
The model effectively distinguishes between legitimate and fraudulent transactions. Key visualizations regarding transaction distributions and correlations can be found in the `visualizations/` directory.

## 🛠️ How to Use
1.  **Clone the repository**: `git clone [your-repo-link]`
2.  **Explore the data**: Check the `Data_Processed/` folder for sample files.
3.  **Run the App**: Navigate to `src/` and run `streamlit run 1_app.py`.
