# E-Commerce Customer Churn Analysis & Automation Predictive Dashboard

![Tools](https://img.shields.io/badge/Tools-Power%20BI%20|%20Python%20|%20Power%20Query-orange)
![Category](https://img.shields.io/badge/Category-Data%20Analytics%20|%20Churn%20Prediction-blue)

## 📌 Project Overview
This project provides a comprehensive end-to-end analysis of customer attrition (churn) for a global e-commerce platform. By integrating historical behavioral data with predictive modeling, the project identifies key drivers of churn and quantifies the financial impact of customer loss. 

The goal is to provide actionable business strategies to recover an estimated **$18.2M in Revenue Loss** through data-driven retention programs.

## 📊 Key Business Insights
* **Revenue Impact:** Identified a total of **$18.2M** in lost revenue from 9% of the customer base.
* **High-Risk Categories:** The **Phone** category is the most vulnerable with a **17% Churn Rate**, followed by **Mobile** at **11%**.
* **Service Friction:** A significant correlation exists between **Customer Complaints** (30% rate) and churn probability.
* **Predictive Performance:** Developed a risk-profiling system to identify customers with a **Churn Probability > 70%** for immediate intervention.

## 🛠️ Data Integrity & Methodology
A critical phase of this project involved a rigorous **Data Audit** to handle extreme technical anomalies:
* **Outlier Remediation:** Identified erroneous `TotalSpend` values reaching quadrillion scales due to data processing noise.
* **Filter Implementation:** Applied a threshold filter in Power Query to exclude records exceeding **$500,000**.
* **Result:** This ensured the integrity of financial reporting, stabilizing the "Lost Revenue" metric at a realistic **$18.2M**.

## 🧮 DAX Measures & Analytics Logic
The following DAX formulas were developed to power the dynamic visualizations and provide deep-dive analytics:

### 1. Core Retention KPIs
```dax
Total Customers = COUNT('final_predictions'[CustomerID])

Total Churn = CALCULATE([Total Customers], 'final_predictions'[Churn] = "Churn")

Churn Rate = DIVIDE([Total Churn], [Total Customers], 0

Lost Revenue = CALCULATE(SUM('final_predictions'[TotalSpend]), 'final_predictions'[Churn] = "Churn")

Revenue at Risk = CALCULATE(SUM('final_predictions'[TotalSpend]), 'final_predictions'[Churn_Prediction] = "Churn")

Complaint Rate = DIVIDE(CALCULATE([Total Customers], 'final_predictions'[Complain] = 1), [Total Customers], 0)

Avg Satisfaction = AVERAGE('final_predictions'[SatisfactionScore])

Avg Tenure = AVERAGE('final_predictions'[Tenure])

Avg Warehouse Distance = AVERAGE('final_predictions'[WarehouseToHome])

Avg Churn Probability = AVERAGE('final_predictions'[Churn_Probability])

High Risk Customers = CALCULATE([Total Customers], 'final_predictions'[Churn_Probability] >= 70)

## 📂 Project Structure
```text
├── data/               # Raw and cleaned datasets
├── models/             # Machine learning model files (if applicable)
├── notebooks/          # Exploratory Data Analysis (EDA)
├── reports/            # Final PDF report and documentation
│   └── figures/        # Dashboard screenshots for documentation
├── src/                # Python scripts for automation and cleaning
└── README.md           # Project lan

## 🖥️ Dashboard Previews
1. Executive Customer Retention Overview
Visualizes high-level financial KPIs, churn rate, and customer composition.<img width="1737" height="817" alt="1  Ecommerce Executive Overview" src="https://github.com/user-attachments/assets/a7e62aa1-83fa-46a5-af40-6a7d70658d64" />

2. Analyzes the impact of complaints and logistics on customer satisfaction.
<img width="1735" height="812" alt="2  Ecommerce Behavior Analysis" src="https://github.com/user-attachments/assets/b6e74888-57cf-409f-aded-c5e2ba1430ff" />

3. Customer Risk Profiling
A proactive lead list for the Customer Success team to execute retention strategies.
<img width="1737" height="806" alt="3  Ecommerce Customer risk   Predictivi Analysis" src="https://github.com/user-attachments/assets/ce711515-9ea1-44d8-b641-e8b82ce57645" />

## 💡 Strategic Recommendations
Service Recovery: Implement a fast-track resolution for complaints in the Phone category to reduce its 17% churn rate.

Predictive Outreach: Use the "High-Risk" Watchlist to target customers with >70% churn probability with personalized incentives.

Logistics Audit: Review shipping costs and lead times for customers located >120 units from warehouses.

👤 Author
https://www.linkedin.com/in/syakirworks/
https://syakirworks-portfolio.base44.app/



