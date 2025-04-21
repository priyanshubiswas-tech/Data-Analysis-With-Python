import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import linregress
import numpy as np  # Import numpy

def draw_plot():
    # Read the data from the CSV file
    try:
        df = pd.read_csv('epa-sea-level.csv')
    except FileNotFoundError:
        print("Error: The file 'epa-sea-level.csv' was not found.")
        return

    # Create a scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='original data', color='blue')

    # Perform linear regression on the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create a range of years to predict up to 2050
    years_full = np.arange(df['Year'].min(), 2051)
    predicted_sea_level_full = slope * years_full + intercept
    plt.plot(years_full, predicted_sea_level_full, 'r', label='Fit All Data')

    # Perform linear regression on data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Create a range of years to predict up to 2050 for the recent data
    years_recent = np.arange(2000, 2051)
    predicted_sea_level_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, predicted_sea_level_recent, 'g', label='Fit since 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return the matplotlib axes object
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == "__main__":
    plot_axes = draw_plot()
    if plot_axes:
        plt.show()