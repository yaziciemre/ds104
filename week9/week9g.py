
import pandas as pd

"""
df = pd.read_csv('week9_dataset_TSMC2014_NYCz.csv')
del df['venueCategoryId']
del df['venueCategory']
del df['timezoneOffset']
df['utcTimestamp'] = pd.to_datetime( df['utcTimestamp'] )
df.to_csv("week9_dataset_TSMC2014_NYCz2.csv")
"""
df = pd.read_csv("week9_dataset_TSMC2014_NYCz2.csv")

"""
users = list(df['userId'].value_counts().to_dict().keys())[0:100]

for u in users:
	sub = df[ df['userId'] == u ]
	print(u, len(sub), sub['utcTimestamp'].max() - sub['utcTimestamp'].min())

"""

cooc = {
	'937-451': 1,
	'937-4596': 4
}


for g in df.groupby(by = ['venueId']):
	cus = list(g[1]['userId'].values)
	cus = list(set(cus))
	if len(cus) > 1:
		for i in cus:




