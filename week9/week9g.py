import numpy as np
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
del df['Unnamed: 0']

"""
users = list(df['userId'].value_counts().to_dict().keys())[0:100]

for u in users:
	sub = df[ df['userId'] == u ]
	print(u, len(sub), sub['utcTimestamp'].max() - sub['utcTimestamp'].min())

"""


df['user'] = df['venueId']
df['venue'] = df['userId']

del df['venueId']
del df['userId']

df['userId'] = df['user']
df['venueId'] = df['venue']

del df['venue']
del df['user']

cooc = {
}

"""
def jaccard( a, b ):
	common = 0
	for i in a:
		for j in b:
			if i == j:
				common += 1
	return common / (len(a) + len(b))
"""
print(df)

for g in df.groupby(by = ['venueId']):
	cus = list(g[1]['userId'].values)
	cus = list(set(cus))
	# cus = [13, 56, 78, 88]
	for i in cus:
		for j in cus:
			if i != j:
				if (i, j) in cooc:
					cooc[ (i,j) ] += 1
				else:
					cooc[ (i,j) ] = 1

user_visits = df['userId'].value_counts().to_dict()


user_user_sim = pd.DataFrame( columns = ['user0', 'user1', 'ratio'] )
"""
for c in cooc:
	if cooc[c] > 1:
		user0 = c[0]
		user1 = c[1]

		user0_count = user_visits[ user0 ]
		user1_count = user_visits[ user1 ]
		ratio = cooc[c] / (user0_count + user1_count)
		
		user_user_sim.loc[ len( user_user_sim) ] = [ user0, user1, ratio ]
		#if ratio >= 0.10 and user0_count > 5 and user1_count > 5:
		#	print(c, ratio, cooc[c], user0_count, user1_count )


print("visit", df.shape)
print("user", df['userId'].nunique())
print("cafe", df['venueId'].nunique())
"""
"""
# Daily average
df['utcTimestamp'] = pd.to_datetime( df['utcTimestamp'] )
items = []
for u in df.groupby(by=['userId']):
	timeline = u[1]['utcTimestamp'].max() - u[1]['utcTimestamp'].min()
	if timeline.days > 0:
		print(u[0], len(u[1]) / timeline.days)
		items.append( len(u[1]) / timeline.days )

print(np.mean(items))
"""


"""
returning customer
for u in df.groupby(by = ['userId']):
	if len(u[1]) > 5:
		print(u[0],  u[1]['venueId'].nunique() / len(u[1])) 
"""