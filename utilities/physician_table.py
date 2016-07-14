# Paste the output of this script in the "physicians" dictionary within the 'physicianlib.py' file.  Replace contents.
# Make sure the updated 'bc_resources.xlsx' file is present in the same directory as this script
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

bc_file_name = 'bc_resources.xlsx'
new_file = 'bc_update.txt'

# read from excel file and add to data frame
bc_data = pd.read_excel(bc_file_name, sheetname="Physicians", skiprows=1)
#print(bc_data.count())

# select only relevant columns from the sheet and reoder
bc_data = bc_data[[2,3,4,6,5,7]]

# convert dataframe into numpy array matrix
bc_data = bc_data.as_matrix()

# convert numpy matrix into list to use in dictionary
bc_data = bc_data.tolist()

# print the list and update physicianlib.py file
print(bc_data)

