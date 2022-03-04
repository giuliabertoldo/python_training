############### DATASET DESCRIPTION ############################
# Data of Walmart stores (chain in the US). 
# We have weekly sales in US dollars in various stores 
# Each sotore has an 
# store = store ID number
# type = store type (A= supercenters, B= discount stores, C=neighborhood markets) 
# department = department ID
# weekly_sales 
# is_holiday = if it was a holiday week or not
# temperature_c = temperature during the week 
# fuel_price = average fuel price in dollars that  week
# unemployment = national unemployment rate that week 
####################################################################

############### TOPICS ############################
# SUMMARY STATISTICS: mean, median, .agg, cumulative stats
# COUNTING: .drop_duplicates, .value_counts
# GROUPED SUMMARY STATISTICS: .groupby(), .pivot_table()
####################################################################

import pandas as pd
import numpy as np

sales = pd.read_csv("data/sales_subset.csv")

# Delete weird column called "Unnamed:0" which is the first column
sales = df.drop(df.columns[[0]], axis=1)

# First few rows 
sales.head()

# Info on each column
sales.info()

######################## SUMMARY STATISTICS ####################### 

# MEAN, MEDIAN, DATES
# Mean column weekly_sales
sales["weekly_sales"].mean()

# Median column weekly_sales 
sales["weekly_sales"].median()

# Date columns (data type datetime64)
# Maximum of date column
sales["date"].max()
# Minimum of date column
sales["date"].min()

# .agg() METHOD
# .agg() method to apply your own custom functions. Syntax:
# df['column'].agg(function)
# Build a function called iqr that calculates the 
# interquartile range (75th percentile - 25th perc.)
def iqr(column):
    high = column.quantile(0.75)
    low = column.quantile(0.25)
    output = high - low 
    return output 
# Use the iqr function to print the iqr of temperature_c
sales['temperature_c'].agg(iqr)
# Use the iqr function to print the iqr of 
# temperature_c fuel_price_usd_per_l unemployment
sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg(iqr)
# include also np.median
sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg([iqr, np.median])

# CUMULATIVE STATISTICS 
# Syntax: df['column'].cumsum()
# Create a dataset called sales_1_1 that contains only 
# the sales data for store A of department 1 
sales_1_1 = sales[(sales['type'] == 'A') & 
                  (sales['department'] == 1)]
sales_1_1.head()
# Sort sales_1_1 by date 
sales_1_1 = sales_1_1.sort_values('date')
# Get the cumulative sum of weekly_sales and 
# add it as a new column of sales_1_1 called cum_weekly_sales.
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()
# Get the cumulative maximum of weekly_sales, and add it as a 
# column called cum_max_sales.
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()
# Print the date, weekly_sales, cum_weekly_sales, and cum_max_sales columns.
print(sales_1_1[['date', 'weekly_sales', 'cum_weekly_sales', 
                'cum_max_sales']])


######################## COUNTING ####################### 

# DROPPING DUPLICATES
# Syntax: df.drop_duplicates(subset=['col1', 'col2'])

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])
store_types.head()

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])
store_depts.head()

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates(subset='date')
holiday_dates['date']

# COUNTING
# Syntax: df['col'].value_counts()
# Syntax: df['col'].value_counts(normalize=True)
# Syntax: df['col'].value_counts(sort=True)

# Use dataset store_types. 
# Count the number of stores of each type
store_types['type'].value_counts()

# Get the proportion of stores of each type
store_types['type'].value_counts(normalize=True)

# Use dataset store_depts. 
# Count the number of each department number and sort
store_depts['department'].value_counts(sort = True)

# Get the proportion of departments of each number and sort
store_depts['department'].value_counts(normalize = True, sort = True)

# GROUPED SUMMARY STATISTICS 
# Syntax: df.groupby('col1')['col2'].mean()
# Syntax: df.groupby('col1')['col2'].agg([min, max])
# Syntax: df.groupby(['col1', 'col2'])['col3'].mean()
# Syntax: df.groupby(['col1', 'col2'])['col3', 'col4'].mean()

# Withough using groupby 
# Calculate the total weekly_sales over the whole dataset.
sales_all = sales['weekly_sales'].sum()
# Subset for type A stores, calc total weekly sales
sales_A = sales[sales['type']=='A']['weekly_sales'].sum()
# Subset for type B stores, calc total weekly sales
sales_B = sales[sales['type']=='B']['weekly_sales'].sum()
# Subset for type C stores, calc total weekly sales
sales_C = sales[sales['type']=='C']['weekly_sales'].sum()
# Get proportion for each type
sales_propn_by_type = [sales_A,sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# With .groupby()
# Group by type; calc total weekly sales
sales_by_type = sales.groupby('type')['weekly_sales'].sum()
# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)
# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)

# Multiple grouped summaries 
# For each store type, aggregate weekly_sales: 
# get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median])
print(sales_stats)
# For each store type, aggregate unemployment and fuel_price_usd_per_l: 
# get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment","fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])
print(unemp_fuel_stats)   

# PIVOT TABLES 
# Syntax: df.pivot_table(values='col1', index='col2')
# Syntax: df.pivot_table(values='col1', index='col2', aggfunc=[func1, func2])
# Syntax: df.pivot_table(values='col1', index='col2', columns='col3', fill_value= 0, margins=True)

# Get the mean weekly_sales by type using
mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type')

# Get the mean and median (using Numpy)of weekly_sales by type 
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=[np.mean, np.median])

# Get the mean of weekly_sales by type and is_holiday 
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales', index='type', columns='is_holiday')

# Print mean weekly_sales by department and type; 
# fill missing values with 0
sales.pivot_table(values='weekly_sales', index='department', columns='type', fill_value=0)

# Print the mean weekly_sales by department and type; 
# fill missing values with 0s; sum all rows and cols
sales.pivot_table(values='weekly_sales', index='department', columns='type', fill_value=0, margins=True)

