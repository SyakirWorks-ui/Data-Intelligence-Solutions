IBM HR Attrition Automation & Analytics
An End-to-End Professional Data Analytics Pipeline
📌 Project Overview
This project delivers a sophisticated, automated solution for analyzing employee attrition patterns using the IBM HR Analytics dataset. By integrating a robust Python-based automation pipeline with an interactive Power BI Executive Dashboard, the project provides stakeholders with actionable insights into workforce stability, compensation fairness, and performance-driven retention.

📂 Project Structure
The repository is architected following industry-standard modularity to separate data processing from business reporting:

Bash

HR-Attrition-Automation/
├── dashboard/
│   └── IBM HR DASHBOARD.pbix       # Multi-page interactive analytics
├── data/
│   ├── raw/                        # Original source data
│   └── processed/                  # Transformed data for BI ingestion
├── docs/                           # Professional reporting layer
│   ├── images/                     # Dashboard captures (Executive, Demographics)
│   ├── reports/                    # Documented summaries and PDFs
│   ├── executive_summary_report.txt# Key findings & business recommendations
│   └── pipeline_log.txt            # Automated validation and processing logs
├── notebooks/                      # Modular analytical development
│   ├── 1data_cleaning.ipynb        # Data preprocessing & type handling
│   ├── 2data_analytics_insights.ipynb # EDA & correlation analysis
│   └── ... (3-5)                   # Automated pipeline & final reporting
├── README.md                       # Comprehensive project documentation
└── setup_project_4.py              # Main pipeline automation engine
🚀 The Automation Pipeline
Unlike static analysis, this project features a Dynamic Automation Engine (setup_project_4.py) that ensures data integrity:

Automated Cleaning: Handles missing values and standardizes data formats across 1,470 employee records.

Execution Logs: Every run is documented in pipeline_log.txt, providing a transparent audit trail for data validation.

Reporting Automation: Generates a text-based executive_summary_report.txt immediately after processing.

📊 Executive Dashboard Insights
The Power BI dashboard transforms raw metrics into strategic narratives:

Attrition Analysis: Identified a baseline 16.12% attrition rate across the organization.

Overtime Impact: Employees working overtime exhibit a critical 30.5% attrition rate, compared to just 10.4% for those who do not.

Financial Metrics: Insights into the $6.5K Average Monthly Income and its correlation with retention.

Visual Excellence: Utilizes interactive slicers for Department, Education Field, and Job Role to enable deep-dive analysis.

💡 Strategic Recommendations
Based on the Executive Summary Report:

Overtime Mitigation: Re-evaluate workload distribution in high-attrition departments to reduce burnout-driven exits.

Retention Focus (Ages 18-25): Implement targeted mentorship for the youngest demographic, which currently shows the highest turnover risk.

Satisfaction Monitoring: Address the 2.73/4.0 average job satisfaction score through employee engagement initiatives.

🛠️ How to Run
Environment Setup: Ensure Python 3.x and Power BI Desktop are installed.

Execute Pipeline: Run python setup_project_4.py to process raw data and generate logs.

Open Dashboard: Navigate to dashboard/ and open the .pbix file to explore interactive visuals.

---
**Author:** [Muhamad Syakirullah](https://www.linkedin.com/in/syakirworks/)  
**Role:** Aspiring Data Analyst  
**Contact:** [syakirworksid@gmail.com] | [https://syakirworks-portfolio.base44.app/]

