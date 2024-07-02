import math
import matplotlib.pyplot as plt
s1 = "week9_diabetes_data.csv"
s2 = "week9_hypertension_data.csv"
s3 = "week9_stroke_data.csv"

import pandas as pd

df1 = pd.read_csv(s1)
df2 = pd.read_csv(s2)
df3 = pd.read_csv(s3)

df3 = df3[ df3['age'] > 0 ]

df3 = df3.dropna()

target3 = 'stroke'

for c in df3.select_dtypes(exclude = ['object']):
	print(c, df3[c].corr(df3[target3]))

for w in df3['work_type'].unique():
	print( w, df3[ df3['work_type'] == w ][target3].mean() )

df3 = pd.get_dummies( df3, columns = ['work_type'])


from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
clf = RandomForestClassifier(max_depth=5, random_state=0)

y = df3[ target3 ]
X = df3.drop(columns = [target3])
clf.fit(X, y)

print(X.columns)
print(clf.feature_importances_)



xs = []
ys = []

ageMap = {}
for i in df3['age'].unique():
	xs.append(i)
	value = df3[ df3['age'] == i ][target3].mean()
	ys.append( value )

	ageMap[ i ] = value

plt.scatter(xs,ys)
# plt.show()


print(df3['age'].describe())
df3['Myage2'] = df3['age'].map(ageMap)
df3['Myage2'] = df3['Myage2'].apply(lambda value: math.pow(value, 4))
print(df3['Myage2'].corr(df3[target3]))
print(df3['age'].corr(df3[target3]))

for i in [43,44,45,46,47,48,49,50,51]:
	df3['Myage'] = df3['age'].apply(lambda value: math.pow(value-i,4.0))
	print(i, df3['Myage'].corr(df3[target3]))



df3['MyageX'] = df3['age'].apply(lambda value: math.pow(value-47,4.0))


dfx_m = df3[ (df3['ever_married'] == 1) & (df3['sex'] == 1) ][target3].mean()
dfx_f = df3[ (df3['ever_married'] == 1) & (df3['sex'] == 0) ][target3].mean()

print(dfx_m, dfx_f)


