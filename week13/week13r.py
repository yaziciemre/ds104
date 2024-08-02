from collections import Counter
from sklearn.cluster import DBSCAN
import numpy as np

s = "bank-additional-full.csv"
import pandas as pd

df = pd.read_csv(s, sep = ";")


for c in list(df.select_dtypes(include = ['object'])):
	df = pd.get_dummies(df, columns = [c] )


for c in df:
	if df[c].nunique() == 2:
		df[c] = df[c].astype(int)

for c in df:
	df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())


del df['euribor3m']
del df['default_no']
del df['housing_unknown']
del df['housing_no']
del df['nr.employed']
del df['y_no']
del df['pdays']
del df['loan_no']
del df['contact_telephone']
del df['poutcome_nonexistent']

for c1 in df:
	for c2 in df:
		if c1 > c2:
			cc = abs(df[c1].corr(df[c2]))
			if cc > 0.80:
				print(c1,c2,cc)

"""
df = df.sample(frac = 0.30)

for c in [0.001, 0.1, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 10, 15, 20]:
	clustering = DBSCAN(eps=c, min_samples=2).fit(df)
	print(c, Counter(list(clustering.labels_)))
"""

from sklearn.cluster import KMeans


for k in [2,3,4,5,6,7,8]:
	kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto").fit(df)
	print( k, c, Counter(list(kmeans.labels_ )))
	df['C'] = kmeans.labels_

	keys = []
	diff = []
	for c in df['C'].unique():
		dd = df[ df['C'] == c ].mean().to_dict()
		dd = {d:round(v,3) for d,v in dd.items()}
		keys = list(dd.keys())
		diff.append(dd)


	print('=========')

# Weekend Assignment:
# Write a function to show how much difference there is, for each clustered centroid of each cluster
# Try to write the silulette score, by yourself



# 7.How can we do feature mining in clustering (there is no target), 
# and how can we determine if we have created good or bad features?
# THERE IS NOT A GOOD SOLUTION

# If quality of a feature is low, we can SKIP
# too much nulls, n,n,n,n,n,n
# most of the values are same (%99) y,y,y,y,y,y,y,y,y,n

# If it is correlated to another
# a --> b (> %90) delete


# a,b,c,d,e,f,g,h columns ==> bad
# a,b,c,d,e,f,g           ==> better
# a,b,c,d,e,f,h           ==> better
# a,b,e,f,h               ==> better

# DUMMY ! city ==> 90 cities, ==> 90 extra columns !! 

# PCA


# 8.What percentage of unique values should a column have to be 
# considered imbalanced, and should we necessarily remove it from 
# the dataset (what kind of problems can it cause)?
# %99 %1, delete 
# %90, %10 --> correlation 0.05, delete


# %X in altinda ==> imbalanced
# 


# 9.When transforming date-type data 
# (e.g., replacing months with their ordinal numbers), 
# this gives more weight to the later months. 
# Instead, is it better to use target averaging?

# May = 5
# Jan = 1
# Dec = 12

# Target Average
# Dummy
# Grouped Dummy (season)
# Grouped Average (season)
# Grouped Binary (summer)
# Grouped Binary (summer, winter)
# Grouped Binary (cold, hot)

# DAY ! DO NOT USE AS NUMERIC VALUE
# Day > 25
# Day < 6


# Education
# prim-sec   = 1
# highschool = 2
# university = 3
# master     = 4
# doc+phd    = 5

# quality of a product
# 


# 10. When should we impute null values in categorical variables? 
#     Is it better to impute nulls before encoding or to impute 
#     them after encoding by using ml? 
#     null values also can cause issues during encoding.

