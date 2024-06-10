
#: Imports
import sys
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np

#: Load
df = pd.read_csv("week6_data.xls")

#: Shuffle
#df = df.sample(frac = 1.0)

l = len(df)

def randomRange( mn, mx ):
	return mn + (mx - mn) * random.random()



# SCENARIO 1: fill mean
# mean: a slightly better than [worst]
# NOTE, in scalar variables, price, high amount useful, measurement, m2, price, huge count(!), wide range data
df['sqft_living'] = df['sqft_living'].fillna( df['sqft_living'].mean() )

# SCENARIO 2: fill mode [most]
# mode: a slightly better than [worst]
# categorical variables, city, country, education level
# waterfront [house has a water view or not ?]
#     0 = no water view
#     1 = water from long distance
#     2 = water from short distance

# city plate number
# 9
# 10
# 77
# 99
# .. avg ==> wrong
most = int(df['waterfront'].mode()[0])
df['waterfront'] = df['waterfront'].fillna( most )

# SCENARIO 3: fill with neighbour [may it is already null, outlier] (later)

# SCENARIO 4: fill 0
# 0 unknown [worst]
# 0 sometimes cannot be understood as None, example: if you fill price with 0, means, pulsuz????
df['view'] = df['view'].fillna(0)

# SCENARIO 5: delete row
# If it is very important for the row(!) like target
# or any column which has 0.60 correlation to target
# df = df.dropna(subset = ['price'])


# SCENARIO 6: delete column
# if the null ratio is "HIGH", we can delete the column!
del df['yr_built']



# SCENARIO 7: estimate
df = df.dropna()
df = df[ df['bedrooms'] > 0 ]

for c in df.select_dtypes(exclude = ['object']):
	print("corr", c, df[c].corr(df['bedrooms']))

df['ratio'] = df['sqft_living'] / df['bedrooms']
print(df['ratio'].describe())


# ev_qiymet = otag x 165000

df['estimate_bedrooms'] = df['sqft_living'] / 627
df.to_csv("week6.csv")
# sqft_living = otag x 627


# SCENARIO 8: null or not [extra column]

df['sqft_above_null'] = df['sqft_above'].isnull()
df['sqft_above'] = df['sqft_above'].fillna( df['sqft_above'].mean() )
print(df[ ['sqft_above_null', 'sqft_above']  ])


# SCENARIO 9: subset avg
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
#df['price'] = df.apply( fillprice, axis = 1 ) # row by row

df.to_csv("week6-x.csv")
print( price_by_bedroom )



# SCENARIO 10: split the dataset
# if there is (one or more) column in dataset and it is important (high correlation)
# if we delete this column, we might lose some information
# if we fill with (random, mean) it will make the column "LESS" correlated

# in this dataset, every column is null (waterfront, view, condition) EMPTY, NULL
ds1 = df[ df['waterfront'].isnull() ]
del ds1['waterfront']
del ds1['condition']
del ds1['view']

# in this dataset, every column (waterfront...view . condition is FULL) no problem
ds2 = df[ df['waterfront'].notnull() ]




# SCENARIO 11: fill with random
# price, amount, random (worst)
df['yr_renovated'] = df['yr_renovated'].fillna( random.random() )

# SCENARIO 12: fill with random in range
# min, max arasinda
mn = df['yr_renovated'].min()
mx = df['yr_renovated'].max()

df['yr_renovated'] = df['yr_renovated'].fillna( randomRange( mn, mx ) )


# SCENARIO 13: fill with random in distribution [mean+std]


# random.random() ===> [0 ile 1] 0.05, 0.6, 0.2342, 0.96058, 0.1243294, 1.0 0.0 0.31431, 0.545352

# random.random() * mx
# 0 ile max arasinda olur

# random.random() + mn
# mn ile mn + 1



for i in range(10):
	print( randomRange(3.5, 17.5) )



for c in df:
	count = len(df[ df[c].isnull() ])
	print(c, count, count / len(df) )


s = np.random.normal(df['sqft_above'].mean(), df['sqft_above'].std(), len(df))
print(s)

data = []
for i in range(1000):
	n = random.random() * 100
	data.append( n )

print(df['sqft_above'].describe())
plt.hist(df['sqft_above'], alpha = 0.50)
plt.hist(s, alpha = 0.50)

# NOTE, plt.hist, scatter, pie,..... alpha = 0.50 %50 transparent

#plt.show()







# hepsine 0 yazsak, cok genel
# better, daha yaxsi? 
# daha spesifik


