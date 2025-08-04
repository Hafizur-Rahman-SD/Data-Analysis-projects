## Page View Time Series Visualizer

This is the Page View Time Series Visualizer project for FreeCodeCamp's Data Analysis with Python certification. This project involves analyzing time series data from a web forum page and visualizing it using different plots to understand patterns, trends, and correlations.

## 📁 Files in the Project

time_series_visualizer.py – Main script that loads data and draws visualizations.

test_module.py – Contains unit tests to verify function correctness.

fcc-forum-pageviews.csv – The dataset containing daily page views.

README.md – This file, describes the project.

## 📊 Data Description

The dataset (fcc-forum-pageviews.csv) contains page view data from May 2016 to December 2019.

The columns are:

date: Date of the observation (daily).

value: Number of page views on that date.

## ✅ Tasks Completed

1. Data Cleaning

Removed the top and bottom 2.5% of data based on the value column to remove outliers.

2. Line Plot

A line plot showing daily page views over time.

Shows overall trend in page views.

3. Bar Plot (Categorical Plot)

Displays average page views per month grouped by year.

Uses Seaborn's catplot() function.

4. Heat Map

Displays correlation of average daily page views by month and day of week.

Uses Seaborn's heatmap() function.

## 📦 Python Libraries Used

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

📂 Project Structure

Page View Time Series Visualizer/
    fcc-forum-pageviews.csv
    time_series_visualizer.py
    test_module.py
    README.md

## ▶️ How to Run the Project

Make sure you have Python and required libraries installed:

pip install pandas matplotlib seaborn

Run the main file:

python time_series_visualizer.py

To run the tests:

python test_module.py

## 📈 Example Outputs

Line Plot: Shows a clear trend in user activity on the forum over time.

Categorical Plot: Displays monthly trends grouped by year.

Heat Map: Highlights patterns based on weekdays and months.

## 📌 Note

Keep the dataset file in the same directory as the Python scripts.

Make sure file names are correct: time_series_visualizer.py, not something else.

## 🏁 Final Thoughts

This project is a great way to practice:

Time series data analysis

Data cleaning with Pandas

Plotting with Matplotlib and Seaborn

Understanding trends and seasonality in data

Author: Hafizur Rahman

GitHub Repo: [https://github.com/Hafizur-Rahman-SD/Data-Analysis-projects]

If you found this project helpful, feel free to give it a ⭐ on GitHub!
                Thank You. 

