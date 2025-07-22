# Workforce Optimization Simulator

## Overview
This project simulates workforce scheduling and load balancing using real-world HR and shift scheduling data. The goal is to detect over/underutilization and optimize workforce assignments based on working hours and team demands.

## Objective
- Simulate employee shift allocation
- Identify over/underutilized employees
- Visualize workforce efficiency
- Generate an optimized workforce distribution report

## Dataset
The combined dataset contains:
- Employee profiles (ID, department, age, experience, satisfaction)
- Weekly shift schedule (binary indicators for each day)
- Workload attributes (weekly hours, projects, overtime)
- Performance scores, promotions, resignations

## Technologies Used
- Python (Pandas, Matplotlib, Seaborn)
- Data preprocessing and cleaning
- Visualization and reporting

## How to Run
```bash
pip install pandas matplotlib seaborn
python workforce_optimizer.py
```

## Workflow
1. Load and combine HR + schedule datasets
2. Calculate weekly hours based on shift patterns
3. Flag underutilized (<50%) and overutilized (>110%) employees
4. Visualize workload distribution and save results

## Results
- Assigned working hours histogram and boxplot
- Overutilization heatmap by group
- Optimization summary in console

## Key Takeaways
- Easy-to-use simulator for staffing diagnostics
- Supports early detection of burnout or inefficiency
- Reusable on new employee scheduling data

## Future Enhancements
- Incorporate forecasting with seasonal shifts
- Dynamic reallocation of teams using optimization algorithms
- Add an interactive Streamlit interface
