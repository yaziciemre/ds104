
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
pca = PCA(n_components=5)
pca.fit(df.drop(columns = ['hospital_death']))
print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.cumsum())
print(pca.singular_values_)

print( pca.transform(df.drop(columns = ['hospital_death'])) )

# 1- dimension reduction, use cases
# Lower dimension ==> lower complexity
# Lower dimension ==> lower time/resource
# Lower dimension ==> less overfitting

# 2- how complex a dataset is?
# complexity of the given dataset
# If we reach 95 percent in a couple of components, that means 
# the dataset is "simple", high correlated

# 3- 