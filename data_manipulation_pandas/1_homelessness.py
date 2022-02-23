############### DATASET DESCRIPTION ############################
# homelessness is a DataFrame containing estimates of homelessness in each 
# U.S. state in 2018. 
# The individual column is the number of homeless individuals not part of 
# a family with children. 
# The family_members column is the number of homeless individuals part of 
# a family with children. 
# The state_pop column is the state's total population.
####################################################################

############### TOPICS ############################
# Exploring a dataframe
# Sorting
# Subsetting 
# Create new columns 
####################################################################

import pandas as pd

df = pd.read_csv("data/homelessness.csv")

# Delete weird column called "Unnamed:0" which is the first column
df = df.drop(df.columns[[0]], axis=1)

############## INTRODUCING DATAFRAMES ######################

# First few rows 
df.head()

# Info on each column
df.info()

# Number of rows and columns
df.shape

# A few summary statistics for each column
df.describe()

# DataFrames consist of 3 components stored as attributes: 
## Two-dimensional NumPy array of values
df.values
## An index of columns: column names
df.columns
## An index for the rows: either row number or row names
df.index

################## SORTING AND SUBSETTING #################### 

# Sort by number of homeless individuals (ascending)
df.sort_values("individuals") 

# Sort by the number of homeless family_members (descending)
df.sort_values("family_members", ascending=False)

# Sort by region, then descending family member
df.sort_values(["region", "family_members"], ascending=[True, False])

# Subset columns: 
# Create a dataframe called individuals that contains 
# only the individuals columns
individuals = df["individuals"]
individuals.head()

# Create a datafreame with only the state and family_members
state_fam = df[["state", "family_members"]]
state_fam.head()

# Create a dataframe with the individuals and state
# columns in that order
ind_state = df[["individuals", "state"]]
ind_state.head()

# Subset rows / Filtering: 
# Filter for cases where the number of individuals is 
# greater than 10000
ind_gt_10k = df[df["individuals"] > 10000]
ind_gt_10k.head()

# Filter for cases where the region is "Mountain"
mountain_reg = df[df["region"] == "Mountain"]
print(mountain_reg)

# Filter for cases where 
# the number of family_members is less than one thousand
# and the region is "Pacific" 
fam_lt_1k_pac = df[(df["family_members"] < 1000) & 
                    (df["region"] == "Pacific")]
print(fam_lt_1k_pac)

# Filter for cases where the region is "South Atlantic"
# or it is "Mid-Atlantic"
regions = ["South Atlantic", "Mid-Atlantic"]
condition = df["region"].isin(regions)
south_mid_atlantic = df[condition]
print(south_mid_atlantic)

# Filter for cases that are in the list canu
canu = ["California", "Arizona", "Nevada", "Utah"]
condition = df["state"].isin(canu)
mojave_homelessness = df[condition]
print(mojave_homelessness)


########################### NEW COLUMNS ########################## 
######### MUTATING | TRANSFORMING | FEATURE ENGINEERING #########

# Add a new column, total, containing the sum of 
# individuals and family_members
df["total"] = df["individuals"]+df["family_members"]

# Add a new column, p_individuals, containing
# the proportion of homeless who are individuals in each state
df["p_individuals"] = df["individuals"]/df["total"]


############## EXERCISE COMBING EVERYTHING ##################### 

# Add a column, indiv_per_10k, with the number of homeless
# individuals per 10 000 people in each state 
df["indiv_per_10k "] = (df["individuals"]*10000)/(df["state_pop"])
df.head()

# Subset rows where indiv_per_10k is higher than 20
high_homelessness = df[df["indiv_per_10k "] > 20]
high_homelessness.head()

# Sort high_homelessness by descending indiv_per_10k
# Error
# high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

