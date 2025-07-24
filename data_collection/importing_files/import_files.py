# import all the necessary libraries for csv, excel ,json,xml,text and sql files 
import pandas as pd 
import json
import xml.etree.ElementTree as ET
import csv
import sqlite3
import pickle 
import joblib
import os

#importing a csv files
csv_data = pd.read_csv("data.csv")
print("CSV file:\n", csv_data.head())

#importing excel files 
excel_data = pd.read_excel("data.xlsx")
print("Excel files data is here:", excel_data.head())

#import an json files 
with open("data.json") as f:
    json_data = json.load(f)
print("\nJson files data is here:", json_data)

#import an XML files 
tree = ET.parse("data.xml")
root = tree.getroot()
print("\nXML file:")
for child in root:
    print(child.tag, child.attrib)

#import text files 
with open("data.txt", "r") as f:
    text_data = f.read()
print("\n Text file is :", text_data)

#impoert from sql data base
conn = sqlite3.connect("data.rb")
sql_data = pd.read_sql_query( "SELECT * FROM your_table", conn)
print("\nSQL Data: ", sql_data.head())

#importing a joblib file 
joblib_data = joblib.load("data.joblib")
print("\n Picke file ", joblib_data)

#importing a pickle file 
with open("data.pkl", "rb") as f:
    pickle_data = pickle.load(f)
print("\nPicke file:", pickle_data)

#importing from a zip file 
zip_data = pd.read_csv("data.zip")
print("\nZIP file", zip_data.head)