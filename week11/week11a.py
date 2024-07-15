
s = "week11_customer_data.csv"
import pandas as pd
df = pd.read_csv(s)

df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
df['loyalty_status'] = (df['loyalty_status'] == 'Regular').astype(int)

df['education'] = df['education'].map({'Masters': 5,  'Bachelor': 3, 'College': 2, 'HighSchool': 1})
df['purchase_frequency'] = df['purchase_frequency'].map({'rare': 1, 'occasional': 3, 'frequent': 6})


for c in df.select_dtypes(exclude = ['object']):
	df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())

dummies = list(df.select_dtypes(include = ['object']).columns)

df = pd.get_dummies( df, dummies )

for c in df.select_dtypes(include = ['bool']):
	df[c] = df[c].astype(int)


from sklearn.cluster import KMeans

# TRAIN TEST YOK !!
# fit(x, y) YOK !!
# score YOK

kmeans = KMeans(n_clusters=4, random_state=0, n_init="auto")
kmeans.fit(df)

cols = df.columns
results = pd.DataFrame(columns = cols)

for c in kmeans.cluster_centers_:
	results.loc[len(results)] = c

print(results)

results.to_csv("week11_clusters.csv")

# Feature weighthing - scoring - importance
# It is the process to give "importance" to each feature!!!
# Feature selecting is the process of subselecting necessary features according to the "importance"

