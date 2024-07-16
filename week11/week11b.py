

# clustering ==~ profiling
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

	if len(g[1]) > 9 and len(g[1]) < 200: # bir user, bir producttan fazla almissa

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


# DO NOT FORGET TO USE THE CODE BELOW, MUST
pivot = pivot.reset_index()
del pivot['user_id']

from sklearn.metrics import silhouette_samples, silhouette_score

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto")
kmeans.fit(pivot)

cluster_labels = kmeans.fit_predict(pivot)
print("silhouette_score", silhouette_score(pivot, cluster_labels))


means = pivot.mean().to_dict()
print(means)

cols = pivot.columns
results = pd.DataFrame(columns = cols)

for c in kmeans.cluster_centers_:
	results.loc[len(results)] = c

for r in results:
	results[r] = results[r] / means[r]

print(results)


results.to_csv("week11b_clusters.csv")




