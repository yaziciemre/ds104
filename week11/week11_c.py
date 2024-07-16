

# clustering ==~ profiling ==~ segmentation
import sys
s = "week11_events.csv"
import pandas as pd
df = pd.read_csv(s)

def onlyMain( i ):
	if "." in str(i):

		# electronics.phone
		# electronics.shavers
		# electronics.laptop
		# main.sub
		# ['electronics', 'laptop']
		return i.split('.')[0]
	return i


df['category_code'] = df['category_code'].apply(onlyMain)

data = []
for g in df.groupby('user_id'):
	# key = g[0],   user_id
	# value = g[1], df[ df['user_id'] == g[0] ] 

	if len(g[1]) > 8 and len(g[1]) < 300: # bir user, bir producttan fazla almissa

		d = g[1]['category_code'].value_counts(normalize=True).to_dict()
		# d = pie chart of a customer, in categories
		# d = percentage distribution of categories for a specific user

		for i in d:
			data.append( [g[0], i, d[i]] )


#: Create a new dataframe
products = pd.DataFrame(
	columns = ['user_id', 'category_code', 'percentage'], 
	data = data)

products.to_csv("week11_out_products.csv")

pivot = products.pivot_table(columns = 'category_code', index = 'user_id', values = 'percentage')
pivot = pivot.fillna(0)
print(pivot.describe().round(5))

pivot.to_csv("week11_out_pivot.csv")

#===================================
# https://stackoverflow.com/questions/29294983/how-to-calculate-correlation-between-all-columns-and-remove-highly-correlated-on
# Find the intercorrelated columns!!
import numpy as np

# Create correlation matrix
corr_matrix = pivot.corr().abs()

# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Find features with correlation greater than 0.95
to_drop = [column for column in upper.columns if any(upper[column] > 0.40)]
print(to_drop)
#===================================

del pivot['electronics']



# DO NOT FORGET TO USE THE CODE BELOW, MUST
pivot = pivot.reset_index()
del pivot['user_id']

from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import DBSCAN

clustering = DBSCAN(eps=0.1, min_samples=5).fit(pivot)

# eps ==> small ==> more clusters!
# eps ==> large ==> less clusters!

# min_samples ==> small ==> more clusters!
# min_samples ==> large ==> less clusters!

data = list(clustering.labels_)


import collections
counter = collections.Counter(data)
print(counter)


# Advantages of dbscan
# - no need to define K , number of clusters
# - there is also possibility to detect ANOMALIES

# Disadvantages of dbscan
# - we cannot label, summarize the cluster

