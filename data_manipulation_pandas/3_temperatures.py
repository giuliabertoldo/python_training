############### DATASET DESCRIPTION ############################
# Temperature dataset: monthly time series of air temperature 
# in cities around the world 
####################################################################

############### TOPICS ############################
# INDEX: CREATE, RESET 
# SUBSET WITH .loc()
# MULTI-LEVEL INDEXES
# SORTING BY INDEX VALUES
# SLICING
# SLICING DATES  
# ACCESS DATE COMPONENTS 
####################################################################

from threading import local
import pandas as pd

temperatures = pd.read_csv("data/temperatures.csv")

# Delete weird column called "Unnamed:0" which is the first column
temperatures = temperatures.drop(temperatures.columns[[0]], axis=1)

# INDEX: CREATE, RESET 
# Look at dataset
print(temperatures)
# Look at rows and columns names
# Syntax: df.columns
# Syntax: df.index 
temperatures.columns
temperatures.index

# Set the index of temperatures to "city"
# Syntax: df.set_index('col') 
temperatures_ind = temperatures.set_index('city')
temperatures_ind

# Reset the index, keeping its contents
# Syntax: df.reset_index()
temperatures_ind.reset_index()

# Reset the index, dropping its contents
# Syntax: df.reset_index(drop=True)
temperatures_ind.reset_index(drop=True)


# SUBSET WITH .loc()
# Syntax: df.loc[list]
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]
# Subset temperatures using square brackets
temperatures[temperatures['city'].isin(cities)]
# Subset temperatures_ind using .loc[]
temperatures_ind.loc[cities]


# MULTI-LEVEL INDEXES
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])
# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]
# Subset for rows to keep
temperatures_ind.loc[rows_to_keep]


# SORTING BY INDEX VALUES 
# Syntax: df.sort_index()
# Syntax: df.sort_index(level='indexname')
# (Instead of sorting on values: .sort_values())

# Sort temperatures_ind by index values
temperatures.sort_index()

# Sort temperatures_ind by index values at the city level
temperatures_ind.sort_index(level ='city')

# Sort temperatures_ind by country then descending city
temperatures_ind.sort_index(level=['country','city'], ascending = [True, False] )


# SLICING 
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
# Syntax: df.loc['':'']
temperatures_srt.loc['Pakistan':'Russia']

# Subset rows from Pakistan, Lahore to Russia, Moscow
# Syntax: df.loc[('':''), ('':'')]
temperatures_srt.loc[('Pakistan', 'Lahore'):('Russia', 'Moscow')]

# Subset rows from India, Hyderabad to Iraq, Baghdad
temperatures_srt.loc[('India', 'Hyderabad'): ('Iraq', 'Baghdad' )]

# Subset columns from date to avg_temp_c
# Syntax: df.loc[:,'':'']
temperatures_srt.loc[:, 'date':'avg_temp_c']

# Subset in both directions at once
temperatures_srt.loc[('India', 'Hyderabad'): ('Iraq', 'Baghdad' ), 'date':'avg_temp_c' ]


# SLICING DATES
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2011-12-31')]
temperatures_bool

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()
temperatures_ind

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
temperatures_ind.loc['2010': '2011']

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
temperatures_ind.loc['2010-08': '2011-02']


# .iloc: SUBSET BY ROW/COLUMN NUMBER
# Get 23rd row, 2nd column (index 22, 1)
temperatures.iloc[22,1]
# Use slicing to get the first 5 rows
temperatures.iloc[:5, ]
# Use slicing to get columns 3 to 4
temperatures.iloc[:, 2:4]
# Use slicing in both directions at once
temperatures.iloc[:5, 2:4]


# ACCESS DATE COMPONENTS : Does not work
# Syntax: df['col'].dt.year
temperatures['date'].dt.year






