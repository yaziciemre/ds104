
#: Imports
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np

#: Load
df = pd.read_csv("week6_data.xls")
df = df.dropna()

def damormertebe( value ):

	if int(value) == value:
		return 'mertebe'
	else:
		return 'dam'


def myfunction( value ):
	if value > 8:
		return 'very large house'
	elif value > 5:
		return 'large house'
	elif value > 3:
		return 'standard house'
	else:
		return 'small house'

df['a'] = df['bedrooms'] / 2
df['b'] = df['bedrooms'] > 2 # large house?

df['c'] = df['bedrooms'].apply( myfunction )
df['damormertebe'] = df['floors'].apply( damormertebe )

df.to_csv("week6c.csv")

print(df)