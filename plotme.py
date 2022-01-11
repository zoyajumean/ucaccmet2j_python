# This script allows you to plot the results from the Python weather assignment.
# You do not need to understand the contents of this script.
# To run, you can click the run button in your IDE (e.g. right top in Visual Studio Code),
#   or you can run `python3 plotme.py` from your terminal (bash or PowerShell).

from plotnine import ggplot
import plotnine as gg
import json
import pandas as pd
import calendar
import os

months = calendar.month_name[1:]  # Get a list of month names

# Open the most extensive dataset available
for part in reversed(range(1, 4)):
    results = None
    filename = f'result{part}.json'
    if os.path.isfile(filename):
        with open(filename) as file:
            results = json.load(file)
        break

# Check that actual data was found and loaded, and if not, terminate the script
if not results:
    print('No valid output files found! Terminating script...')
    exit()

# Define which properties exist in the dataset
properties = ['month', 'totalMonthlyPrecipitation']
if part >= 2:
    properties += ['relativeMonthlyPrecipitation']

# Convert data to a properly formatted DataFrame
results = pd.json_normalize([{'city': city, **data} for city, data in results.items()])
results['month'] = [months] * len(results)
data = results.explode(properties)

# Convert data to correct types
data['month'] = pd.Categorical(data['month'], categories=months)
data['totalMonthlyPrecipitation'] = data['totalMonthlyPrecipitation'].astype(float)
if part >= 2:
    data['relativeMonthlyPrecipitation'] = data['relativeMonthlyPrecipitation'].astype(float)

# Ensure the figures folder exists
if not os.path.exists('figures'):
    os.makedirs('figures')

# Draw a bar plot of the precipitation in Seattle per month
figure_1 = (
    ggplot(gg.aes(x='month', y='totalMonthlyPrecipitation'), data=data[data.city == 'Seattle']) +
    gg.geom_col() +
    gg.theme(axis_text_x=gg.element_text(angle=-30, hjust=0)) +
    gg.labs(x=None, y='Precipitation (mm)')
)
figure_1.save('figures/figure1.pdf')

# If part 2 was reached, draw a bar plot of the relative precipitation in Seattle per month
if part >= 2:
    figure_2 = (
        ggplot(gg.aes(x='month', y='relativeMonthlyPrecipitation'), data=data[data.city == 'Seattle']) +
        gg.geom_col() +
        gg.theme(axis_text_x=gg.element_text(angle=-30, hjust=0)) +
        gg.labs(x=None, y='Proportion of yearly precipitation')
    )
    figure_2.save('figures/figure2.pdf')

# If part 3 was reached, plot two figures: a faceted bar plot of the relative montly precipitation per city,
#   and a stacked barplot of the total monthly precipitation per city.
if part == 3:
    figure_3a = (
        ggplot(gg.aes(x='month', y='relativeMonthlyPrecipitation', fill='city'), data=data) +
        gg.geom_col(position=gg.position_dodge()) +
        gg.theme(axis_text_x=gg.element_text(angle=-30, hjust=0)) +
        gg.facet_wrap('city') +
        gg.labs(x=None, y='Proportion of yearly precipitation', fill='City')
    )
    figure_3a.save('figures/figure3a.pdf')

    figure_3b = (
        ggplot(gg.aes(x='city', y='totalMonthlyPrecipitation', fill='month'), data=data) +
        gg.geom_col() +
        gg.theme(axis_text_x=gg.element_text(angle=-30, hjust=0)) +
        gg.labs(x=None, y='Precipitation (mm)', fill='Month')
    )
    figure_3b.save('figures/figure3b.pdf')
