##import necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Draw load data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Scatter plot banano
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # 3. First line of best fit (shob data niye)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(df['Year'].min(), 2051))
    y_all = res_all.intercept + res_all.slope * x_all
    plt.plot(x_all, y_all, 'r', label='Fit: all data')

    # 4. Second line of best fit (2000 theke shuru kore)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = pd.Series(range(2000, 2051))
    y_2000 = res_2000.intercept + res_2000.slope * x_2000
    plt.plot(x_2000, y_2000, 'green', label='Fit: 2000 onwards')

    # 5. Labels, title, legend add koro
    ax = plt.gca()   # Current axis object
    ax.set_xlabel('Year')                       # Label set kora axis object diye
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # 6. Plot save kora and show kora
    plt.savefig('sea_level_predector.png')
    plt.show()

    # 7. Axis return kore (testing er jonno)
    return plt.gca()

# Function run kore
draw_plot()
