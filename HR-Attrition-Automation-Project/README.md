# IBM HR Analytics: Workforce Insights & Attrition Automation

This project provides a comprehensive data analysis of human resource metrics to identify patterns in employee performance, engagement, and attrition. By leveraging data-driven insights and a robust Python-based automation pipeline, this analysis aims to support HR departments in making strategic decisions to improve employee retention and workforce productivity.

## 📌 Project Overview
The core objective of this analysis is to explore the factors influencing employee turnover and performance. This includes analyzing salary distributions, department-specific trends, and the critical correlation between employee satisfaction, overtime work, and retention rates.

## 📂 Repository Structure
The project is organized into modular directories to ensure transparency and reproducibility of the analysis:

* **dashboard/**: Contains the final interactive Power BI dashboard (`.pbix`) with multi-page analytics including Executive Overview and Performance Analysis.
* **data/**: Divided into `raw/` for the original IBM dataset and `processed/` for the cleaned versions used in the final analysis.
* **docs/**: The professional reporting layer containing:
    * `images/`: High-resolution dashboard captures for quick stakeholder review.
    * `reports/`: Documented executive summaries and PDF analysis.
    * `executive_summary_report.txt`: Strategic business findings and recommendations.
    * `pipeline_log.txt`: Automated validation logs ensuring data integrity throughout the process.
* **notebooks/**: Contains Jupyter Notebooks documenting the modular step-by-step development from Data Cleaning to Exploratory Data Analysis (EDA).
* **setup_project_4.py**: The main automation engine that executes the end-to-end data pipeline and generates real-time reports.
  
## 📊 Dashboard Preview
## 1. Executive Overview
Comprehensive view of key HR metrics including Attrition Rate, Employee Count, and Income trends.
<img width="1737" height="817" alt="1  Executive Dashboard" src="https://github.com/user-attachments/assets/e28a02aa-a0a0-4e30-9540-f5e2b85ce459" />
## 2. Demographics & Attrition Drivers
Deep dive into attrition by Age, Gender, Marital Status, and Environment Satisfaction.
<img width="1730" height="817" alt="2  Demographics   Drivers" src="https://github.com/user-attachments/assets/c17b8dd5-2ce8-49db-ab89-84446315f1b0" />
## 3. Performance & Compensation Analysis
Correlation between Salary Hikes, Performance Ratings, and Promotion cycles.
<img width="1741" height="817" alt="3  Performance   Compensation Analysis" src="https://github.com/user-attachments/assets/cfab0ba4-c34c-4be8-90c6-9baf16325687" />

## 🧪 Technical Implementation (Complete DAX Documentation)
To enable the dynamic interactivity of this dashboard, I developed a centralized library of measures within the All Measure folder.

## 1. Core Workforce Metrics
Fundamental calculations to establish the organization's current scale.
**Total Employees** = COUNT('HR_Final_Gold_Standard'[EmployeeID])

**Total Employees** = COUNT('HR_Final_Gold_Standard'[EmployeeID])

**Active Employees** = CALCULATE([Total Employees], 'HR_Final_Gold_Standard'[Attrition] = "No")

**Attrition Count** = CALCULATE([Total Employees], 'HR_Final_Gold_Standard'[Attrition] = "Yes")

**Attrition Rate** = DIVIDE([Attrition Count], [Total Employees], 0)

## 2. Demographic & Tenure Analytics
Quantifying the profile of the workforce to identify risk groups.

**Avg Age** = AVERAGE('HR_Final_Gold_Standard'[Age])

**Avg Tenure** = AVERAGE('HR_Final_Gold_Standard'[YearsAtCompany])

**Female Count** = CALCULATE([Total Employees], 'HR_Final_Gold_Standard'[Gender] = "Female")

**Male Count** = CALCULATE([Total Employees], 'HR_Final_Gold_Standard'[Gender] = "Male")

## 3. Behavioral & Satisfaction Insights
Deep analytical measures relating work environment to attrition.

**Avg Job Satisfaction** = AVERAGE('HR_Final_Gold_Standard'[JobSatisfaction])

**Avg Monthly Income** = AVERAGE('HR_Final_Gold_Standard'[MonthlyIncome])

**Overtime Impact** = DIVIDE(
    CALCULATE([Total Employees], 'HR_Final_Gold_Standard'[OverTime] = "Yes" && 'HR_Final_Gold_Standard'[Attrition] = "Yes"),
    CALCULATE([Total Employees], 'HR_Final_Gold_Standard'[OverTime] = "Yes"),
    0
)

## 💡 Key Analytical Insights
**Overtime Burnout & Attrition**: Employees working overtime exhibit a critical attrition rate of 30.53%, which is nearly triple the rate of those who do not (10.44%), signaling a high risk of burnout.

**Business Travel Vulnerability**: Frequent travelers have the highest turnover at 24.91%, indicating that high-mobility roles require stronger retention incentives or better work-life balance support.

**Tenure & Career Lifecycle**: Attrition is most volatile during the initial 0-2 years of service (early-career turnover) and spikes significantly after 35+ years, suggesting gaps in both onboarding and long-term succession planning.

**Engagement & Involvement Link**: There is a direct correlation between engagement and loyalty; Level 1 Job Involvement leads to a massive 33.73% turnover, whereas Level 4 involvement reduces it drastically to only 9.03%.

**Demographic Risk (Age & Marital Status**: The 18-25 age group is the most vulnerable with a 39.18% attrition rate. Furthermore, Single employees (Male: 26.94%, Female: 23.62%) are much more likely to leave compared to married or divorced counterparts.

**Environment Satisfaction Impact**: Low environment satisfaction (Level 1) results in 25.35% attrition, but improving this to Level 2 drops the rate by nearly 10%, showing the immediate ROI of improving workplace culture.

**Compensation & Role Benchmarks**: Managers and Research Directors hold the highest monthly incomes, yet high-stress roles like Sales Representatives face the highest turnover despite an average organizational salary hike of $6.5K.

**Promotion Paradox**: Attrition shows sharp peaks for employees who have gone 0-1 years or 15 years without a promotion, indicating that "too early" or "too late" career movements are both critical exit points.

## 💡 Strategic Recommendations
Based on the data-driven insights, the following actions are recommended to improve employee retention:

**Overtime Mitigation**: Implement a workload monitoring system to identify employees consistently working overtime and introduce mandatory rest periods or additional resource allocation to prevent burnout.

**Early-Career Mentorship**: Develop a robust 2-year "New Joiner" mentorship program specifically for the 18-25 age group and Sales department to increase engagement during the most vulnerable tenure period.

**Environment & Culture Enhancement**: Prioritize workplace environment improvements for departments reporting Level 1 satisfaction, as data shows even a small increase in satisfaction can significantly reduce turnover.

**Travel Policy Review**: For roles requiring frequent business travel, consider offering "travel-free" weeks or additional remote work flexibility to offset the high attrition associated with frequent mobility.

## 📂 How to Explore
**1. Quick Review**: View the screenshots in the Dashboard Preview section above.

**2.Full Logic Review**: All DAX formulas are documented in the Technical Implementation section.

**3.Live Interaction**: Download the .pbix file from the /dashboard folder to interact with the filters and data model directly.

## 🤝 Contact & Feedback
I am always open to discussing data-driven strategies and technical implementations.

**LinkedIn**: [https://www.linkedin.com/in/syakirworks/]

**Email**: [syakirworksid@gmail.com]

**Website**: [https://syakirworks-portfolio.base44.app/]

