import pandas as pd
from pathlib import Path

# Correct path to the CSV file
data = Path('data') / 'employee_data.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(data)

# Print the DataFrame
print(df.head())
print(df.describe())
