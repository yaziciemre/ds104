
#: Imports
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np

#: Load
df = pd.read_csv("week6_data.xls")


def fillrenovated( value ):
	if value == None or pd.isna(value) or pd.isnull(value):
		return random.random() # called EACH TIME
	else:
		return value

# price, amount, random (worst)
rnd = random.random()  # 0.55


# called only once!!
# df['yr_renovated'] = df['yr_renovated'].fillna( random.random() ) # called for each cell, grouply, fillna passes the constant value
df['yr_renovated'] = df['yr_renovated'].apply( fillrenovated ) # called for each cell, indivually



df.to_csv("week6d.csv")
print( df['yr_renovated'] )

"""
# Below approach is extremely slow, not suggested!!
for i in range(len(df)):
	value = df.iloc[ i ]['yr_renovated']
	if value == None or pd.isna(value) or pd.isnull(value):
		df.loc[i, 'yr_renovated'] = random.random()
"""

