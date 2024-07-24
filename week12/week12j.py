
import sys
import math
import random
s = "week12_patientdataset.csv"
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(s)
df['gender'] = df['gender'].map({'M': 1, 'F':0})
df = df.dropna()

#df.to_csv("week12_patientdataset_small.csv")


# WARNING, ONLY FOCUSES ON LINEARS!!
import numpy as np
from sklearn.decomposition import PCA
#! PCA is UNSUPERVISED, TARGET INDEPENDET

pca = PCA(n_components=3)
pca.fit(df.drop(columns = ['hospital_death']))
print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.cumsum())
print(pca.singular_values_)

transformed = pca.transform(df.drop(columns = ['hospital_death']))
print( transformed )


# One of the dimension reduction algorithms: PCA, .....
# princibal ==> primary component analysis

# 1- dimension reduction, use cases
# Lower dimension ==> lower complexity
# Lower dimension ==> lower time/resource
# Lower dimension ==> less overfitting

# 2- how complex a dataset is?
# complexity of the given dataset
# If we reach 95 percent in a couple of components, that means 
# the dataset is "simple", high correlated

# 3- Feature importances are already highlighted
# So that we can use this criteria in feature selection

# 4- Visualization
# We can visualize 2 dimension data using pca, which has been reducted from 74 to 2 (x,y)
#plt.scatter( transformed[:,0], transformed[:,1] )
#plt.show()

# 5- Feature engineering
# In a way

# NOTE: 
dx = pd.DataFrame( transformed )
dx.columns = ['0', '1', '2']
#dx = dx[ dx['0'] < -350 ]
#dx = dx.sort_values( by = ['0'] )
#print(dx)
weights = list(pca.explained_variance_ratio_)


print(df.shape)
print(dx.shape)

df = df.reset_index()
dx = dx.reset_index()

df['COMP0'] = dx['0']



def weighted_euclidean( rowA, rowB, weights ):
	distance = 0

	rowA = rowA.values
	rowB = rowB.values
	for i in range(len(weights)):
		distance += pow(rowA[i] - rowB[i], 2.0) * weights[i]

	distance = distance / sum(weights)
	distance = math.sqrt(distance)

	return distance


labeled_items = []

for _ in range(3):
	rowA = dx.iloc[ random.randint(0, len(dx) - 1) ] # --> LABEL [crash  350 manat]
	rowB = dx.iloc[ random.randint(0, len(dx) - 1) ]

	if weighted_euclidean( rowA, rowB, weights ) < 50:
		# DO NOT LABEL, because it is very similar to first one
		pass
	else:
		# LABEL
		pass


# 6- Distance
# We can use the weighted euclidean here, safely!
# Where as the weights are obtained from explained_variance_ratio_

# 7- Ranking
# We can rank the records by similarity (!)

# 8- Distance to the center ==> ANOMALY or NOT, close border?
# If a record's component values are close to "0" it means it is very close
# to the center (mean of dataset)
# 
# if the values are very low ==> close to the mean (average, center)
# if the values are very HIGH ==> very FAR AWAY FROM mean (average, center)

#randomRow = df.iloc[ random.randint(0, len(df) - 1) ]
#del randomRow['hospital_death']
#print( pca.transform( [ randomRow ] ) )
#print( pca.transform( [df.drop(columns = ['hospital_death']).mean()] ) )

# 9- Clustering
# We can use pca before clustering

# 10- Bi-Dimension Reduction
del df['COMP0']

df0 = df[ df['hospital_death'] == 0 ]
df1 = df[ df['hospital_death'] == 1 ]

del df0['hospital_death']
del df1['hospital_death']

pca0 = PCA(n_components=1)
pca0.fit(df0)
tr0 = pca0.transform( df0 )

pca1 = PCA(n_components=1)
pca1.fit(df1)
tr1 = pca1.transform( df1 )


#plt.scatter( tr0[:,0], tr0[:,1] )
#plt.scatter( tr1[:,0], tr1[:,1] )
#plt.show()


y = df['hospital_death']
del df['hospital_death']
p0 = pca0.transform(df)
p1 = pca1.transform(df)

#! df['p0'] = p0
#! df['p1'] = p1
df['hospital_death'] = y


df.to_csv("week12_j.csv")
del df['index']

# DISADVANTAGES of PCA / DIMENSION REDUCTION

# *** LOW CORRELATION: because it only focuses on linear variables, the obtained features may not be useful
# *** EXPLAINABILITY : because it only uses "component names as 0, 1, 2", it is very difficult to explain to business department


# 11- Merge the low correlated items into ONE dimensional data

columns_to_delete = []
for c in df:
	corr = df[c].corr(df['hospital_death'])
	if abs(corr) < 0.10:
		columns_to_delete.append(c)

print(columns_to_delete, len(columns_to_delete))

print("silinecek")
silinecek = df[ columns_to_delete ]
pca_silinecek = PCA(n_components=1)
pca_silinecek.fit(silinecek)
df['SILINMIS'] = pca_silinecek.transform( silinecek )

df = df.drop(columns = columns_to_delete)
print(df.shape)

df.to_csv("week12_j.csv", index = None)




from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

clf = LinearDiscriminantAnalysis()
clf.fit(df.drop(columns = ['hospital_death']), df['hospital_death'])
r = clf.predict( df.drop(columns = ['hospital_death']) )

df['LDA_result'] = r
print(df['LDA_result'].corr(df['hospital_death']))

