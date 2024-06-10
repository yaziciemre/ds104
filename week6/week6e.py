

#: Imports
import sys
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np

#: Load
df = pd.read_csv("week6_data.xls")
df = df.dropna( subset = ['bedrooms'])

# In cases where the variable has a small number of values (1...9)
# if df['x'].nunique() < 10

price_by_bedroom = df.groupby(by = ['bedrooms'])['price'].mean().to_dict()
print(price_by_bedroom)

def fillprice( row ):
	value = row['price']
	if value == None or pd.isna(value) or pd.isnull(value):
		return price_by_bedroom[ row['bedrooms'] ]
	else:
		return value

# df['price'] = df['price'].apply( function )
# send the whole "ROW" to the function
df['price'] = df.apply( fillprice, axis = 1 ) # row by row

df.to_csv("week6-x.csv")
print( price_by_bedroom )
