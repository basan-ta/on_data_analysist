import pandas as pd
import numpy as np

#Creating a sample dataframe 

data = {
    'id' : [1, 2, 3, 4, 5,6, 7, 8, 9, 10],
    'name': ['Ram','Sudip','Dkc','suwash','pawan','katteldae','sujan','pratik','rijan','binam'],
    'age':[23,24,24,23,23,23,23,23,24,24],
    'salary': [35000,25000,34000,21000,20000,26000,25000,29000,29000,29000],
    'city': ['Kathmandu','bangey','Kathmandu','butwal','jhaapa','jhapa','dhangadi','urlabari','biratnagr','rajarani'],
}
df = pd.DataFrame(data)

#printing the  dataframe
print(df.head())

#printing summary of dataframe
print(df.describe())

#printing techniacal summuary of dataframe
print(df.info())

#Printing the values of the df in 2D array format
print(df.values)

#row and column with index and column 
print(df.index)
print(df.columns)

#Printing the shape of the dataframe
print(df.shape)