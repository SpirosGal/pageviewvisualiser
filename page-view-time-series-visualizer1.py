import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975)) 
    ]  
df['date'] = pd.to_datetime(df['date'])


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(18, 5))
    plt.plot(df['date'], df['value'], color='red')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7], interval=6))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Convert date strings to datetime objects
    start_date = datetime.strptime('2016-07', '%Y-%m')
    end_date = datetime.strptime('2020-01', '%Y-%m')

    plt.xlim(start_date, end_date)
    # plt.xticks(rotation=90)
    plt.tight_layout()

    # Save image
    fig = plt.gcf()  # Get the current figure
    fig.savefig('line_plot.png')
    return fig
  
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar plot
    df_bar['date'] = pd.to_datetime(df_bar['date'])

    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month
    unique_months = df_bar['month'].unique()
    colors = sns.color_palette('tab20', n_colors=len(unique_months)) #get a color for each month
    month_names = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }

    result = df_bar.groupby(['year', 'month'])['value'].sum().unstack()

    plt.figure(figsize=(10, 6))
    num_years = len(result)
    bar_width = 0.6 / len(unique_months)

    for i, month in enumerate(unique_months):  
        month_name = month_names[month]
        x_values = np.arange(num_years) + (i - len(unique_months)/2) * bar_width
        plt.bar(x_values, result[month],  color=colors[i], label=month_name) #give the same color if month is repeted 

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    plt.xticks(np.arange(num_years), result.index, rotation=45)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x)}')) 
    plt.legend(title='Months',  labels=[month_names[i] for i in range(1, 13)]) 

    plt.tight_layout()

    # Create the fig object
    fig = plt.gcf()  # Get the current figure

    # Save image
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    plt.figure(figsize=(15, 10))
    
    # Y-axis formatter function
    def y_axis_formatter(x, pos):
        if x >= 1e6:
            return f'{int(x/1e6)}M'
        return f'{int(x)}'

    y_format = FuncFormatter(y_axis_formatter)

    # Year-wise Box Plot (Trend)
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')
    
    # Set custom y-axis ticks and labels
    y_ticks = [0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
    plt.yticks(y_ticks, labels=[y_axis_formatter(val, None) for val in y_ticks])

    # Month-wise Box Plot (Seasonality)
    plt.subplot(1, 2, 2)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, order=month_order)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')
    
    # Set custom y-axis ticks and labels
    y_ticks = [0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
    plt.yticks(y_ticks, labels=[y_axis_formatter(val, None) for val in y_ticks])

    plt.tight_layout()

    # Create the fig object
    fig = plt.gcf()  # Get the current figure

    # Save image
    fig.savefig('box_plot.png')
    return fig
