import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,5))
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    res = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(1880,2051)])
    y = res.slope * x + res.intercept
    plt.plot(x , y , 'g', label="1880-2050 predict")
    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    res2 = linregress(new_df['Year'],new_df['CSIRO Adjusted Sea Level'])
    x2 = pd.Series([i for i in range(2000,2051)])
    y2 = res2.slope * x2 + res2.intercept
    plt.plot(x2 , y2, 'r', label="2000-2050 predict")

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
