import pandas as pd
from pathlib import Path

# Correct path to the CSV file
data = Path('data') / 'employee_data.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(data)

#print dataset 
#print(df)

#Subsetting with index 
#1 Set the index of employee_data to name 
name_index = df.set_index('name')


# Look at df
print(name_index)

# Reset the df index, keeping its contents
print(name_index.reset_index())

# Reset the df index, dropping its contents
print(name_index.reset_index(drop=True))