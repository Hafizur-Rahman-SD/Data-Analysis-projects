# Medical Data Visualizer

This project is part of the freeCodeCamp Data Analysis certification.  
It focuses on analyzing and visualizing medical examination data using Python libraries such as Pandas, Seaborn, and Matplotlib.

---

## Project Overview

The dataset contains medical examination data of patients, including body measurements, blood pressure readings, cholesterol and glucose levels, lifestyle habits, and cardiovascular disease presence.

The goal of this project is to:

- Add a new feature (`overweight`) based on BMI calculation.
- Normalize certain features (`cholesterol` and `gluc`) into binary indicators.
- Create a **Categorical Plot** to compare counts of various health indicators among patients with and without cardiovascular disease.
- Create a **Heatmap** to visualize correlations among medical variables, after cleaning the data to remove inconsistent and outlier records.

---


## How the Code Works

1. **Data Loading**  
   The medical data is loaded from the CSV file into a Pandas DataFrame.

2. **Feature Engineering**  
   - The BMI is calculated and used to create an `overweight` column (1 if BMI > 25, else 0).  
   - Cholesterol and glucose levels are normalized to 0 (good) or 1 (bad).

3. **Categorical Plot**  
   - Data is transformed into a long format suitable for plotting.  
   - Bar charts show counts of various health indicators grouped by cardiovascular disease status.

4. **Heatmap**  
   - Data is cleaned by removing inconsistent records (e.g., diastolic pressure higher than systolic).  
   - Outliers in height and weight are removed using percentile filters.  
   - A correlation matrix is computed and visualized using a heatmap to reveal relationships between variables.

---

## How to Run

- Make sure you have Python installed (recommended version 3.6+).  
- Install required libraries using pip:

  ```bash
  pip install pandas seaborn matplotlib numpy



## Author
This project is completed by Hafizur-Rahman-SD as part of the freeCodeCamp Data Analysis Certification.

