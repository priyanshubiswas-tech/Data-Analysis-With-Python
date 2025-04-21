import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    # Read the data and set the index
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

    # Clean the data
    df_cleaned = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Create the line plot
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(df_cleaned.index, df_cleaned['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def draw_bar_plot():
    # Read the data and set the index
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

    # Clean the data
    df_cleaned = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Create year and month columns
    df_cleaned['year'] = df_cleaned.index.year
    df_cleaned['month'] = df_cleaned.index.month_name()

    # Calculate the average page views per month grouped by year
    df_bar = df_cleaned.groupby(['year', 'month'])['value'].mean().unstack()

    # Define the order of the months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[month_order]

    # Create the bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 8))
    plt.title('Average Daily Page Views per Month Grouped by Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.xticks(rotation=0)
    plt.legend(title='Months')
    plt.tight_layout()
    return fig

def draw_box_plot():
    # Read the data and set the index
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

    # Clean the data
    df_cleaned = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Create year and month columns
    df_box = df_cleaned.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Create the figure and subplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=month_order)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    line_plot = draw_line_plot()
    line_plot.savefig('line_plot.png')
    bar_plot = draw_bar_plot()
    bar_plot.savefig('bar_plot.png')
    box_plot = draw_box_plot()
    box_plot.savefig('box_plot.png')
    print("Plots saved as line_plot.png, bar_plot.png, and box_plot.png")