import sys
import math
import numpy as np
s = "week6_diabetes_prediction_dataset.csv"
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(s)

# Transformation & Feature mining, Feature engineering
df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})

print(df.select_dtypes(exclude = ['object']).corr())


def ageLevel( age: int ) -> int:
	if age < 30: return 1
	if age < 39: return 2
	if age < 54: return 3
	if age < 60: return 4
	return 5

# FM1: Trimming
df['age_1'] = df['age'] / 10.0
df['age_1'] = df['age_1'].astype(int)

# FM2: Rounding
df['age_2'] = df['age'] / 10.0
df['age_2'] = df['age_2'].round()

# FM3: Boundary - limit
df['age_3'] = df['age'] > 39

# FM4: Boundary - limit: mean
df['age_4'] = df['age'] > df['age'].mean()

# FM5: Limits, levels
df['age_5'] = df['age'].apply( ageLevel )

# FM6: Sqrt
df['age_6'] = df['age'].apply( lambda value: math.sqrt(value) )

# FM7: Power
df['age_7a'] = df['age'].apply( lambda value: math.pow(value, 1.65) )
df['age_7b'] = df['age'].apply( lambda value: math.pow(value, 1.70) )
df['age_7c'] = df['age'].apply( lambda value: math.pow(value, 1.75) )

# FM8: Log
df['age_8'] = df['age'].apply( lambda value: np.log(value) )

# FM9: Weighting
weights = {}
for i in range(int(df['age'].min()), int(df['age'].max())+1):
	weights[ i ] = df[ df['age'] == i ]['diabetes'].mean()

df['age_9'] = df['age'].map( weights )




cols = ['age','age_1','age_2','age_3','age_4','age_5','age_6','age_7a','age_7b','age_7c','age_8', 'age_9']

for c in cols:
	print(c, df[c].corr(df['diabetes']))


"""
labels = []
data = []
for i in range(int(df['age'].min()), int(df['age'].max())):
	labels.append(i)
	data.append( df[ df['age'] == i ]['diabetes'].mean())


plt.scatter( labels, data )
plt.show()

"""

# blood_glucose_level
cols = ['blood_glucose_level', 'bgl_1', 'bgl_2', 'bgl_10a', 'bgl_10b', 'bgl_10c', 'bgl_10d', 'bgl_10e', 'bgl_3a', 'bgl_3b', 'bgl_3c', 'bgl_3d', 'bgl_3e', 'bgl_3f']

df['bgl_1'] = df['blood_glucose_level'] / 10
df['bgl_1'] = df['bgl_1'].astype(int)

df['bgl_2'] = df['blood_glucose_level'] / 10
df['bgl_2'] = df['bgl_2'].round()

# FM 10: Ranges
df['bgl_10a'] = df['blood_glucose_level'].apply( lambda value: value <= 125 and value >= 100)
df['bgl_10b'] = df['blood_glucose_level'].apply( lambda value: value <= 199 and value >= 140)
df['bgl_10c'] = df['blood_glucose_level'].apply( lambda value: value <= 99 and value >= 72)
df['bgl_10d'] = df['blood_glucose_level'].apply( lambda value: value <= 130 and value >= 70)
df['bgl_10e'] = df['blood_glucose_level'].apply( lambda value: value <= 110 and value >= 79)

# FM3-alternative:
df['bgl_3a'] = df['blood_glucose_level'] > df['blood_glucose_level'].quantile(0.90) + 1
df['bgl_3b'] = df['blood_glucose_level'] > df['blood_glucose_level'].quantile(0.90)
df['bgl_3c'] = df['blood_glucose_level'] > df['blood_glucose_level'].quantile(0.90) - 1

df['bgl_3d'] = df['blood_glucose_level'] > 190
df['bgl_3e'] = df['blood_glucose_level'] > df['blood_glucose_level'].quantile(0.15)
df['bgl_3f'] = df['blood_glucose_level'] > df['blood_glucose_level'].quantile(0.20)


print('quantile', df['blood_glucose_level'].quantile(0.90))

for c in cols:
	print(c, df[c].corr(df['diabetes']))


"""

labels = []
data = []
for i in range(int(df['blood_glucose_level'].min()), int(df['blood_glucose_level'].max())):
	labels.append(i)
	data.append( df[ df['blood_glucose_level'] == i ]['diabetes'].mean())

plt.scatter( labels, data )
plt.show()
"""


def isGoodBMI( row ):

	age = row['age']
	bmi = row['bmi']

	if age >= 20 and age <= 65:
		if bmi <= 18.5:
			return 1
		elif bmi <= 24.9:
			return 2
		elif bmi <= 29.9:
			return 3
		else:
			return 4

	if age > 65:
		if bmi < 27:
			return 2
		else:
			return 3


	return 1



df['goodbmi'] = df.apply(lambda row: isGoodBMI(row), axis = 1)


df['goodbmi-x'] = df['bmi'] > 30.0
#If your BMI is less than 18.5, it falls within the underweight range. 
#If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range. 
#If your BMI is 25.0 to 29.9, it falls within the overweight range. 
#If your BMI is 30.0 or higher, it falls within the obese range.



print(df['goodbmi-x'].corr(df['diabetes']))

"""
df['HbA1c_level'] = (df['HbA1c_level'] - df['HbA1c_level'].min()) / (df['HbA1c_level'].max() - df['HbA1c_level'].min())
df['blood_glucose_level'] = (df['blood_glucose_level'] - df['blood_glucose_level'].min()) / (df['blood_glucose_level'].max() - df['blood_glucose_level'].min())


column = 'HbA1c_level'
labels = []
data = []
for i in df[column].unique():
	labels.append(i)
	data.append( df[ df[column] == i ]['diabetes'].mean())

plt.scatter( labels, data )


column = 'blood_glucose_level'
labels = []
data = []
for i in df[column].unique():
	labels.append(i)
	data.append( df[ df[column] == i ]['diabetes'].mean())

plt.scatter( labels, data )

plt.show()
"""




df['mynewfeature1'] = (df['HbA1c_level'] > 5.5) & (df['bmi'] > 40)

df['mynewfeature3'] = df['age'] + df['bmi']
df['mynewfeature3'] = df['mynewfeature3'] > 85


df['mynewfeaturec1'] = df['age'] * df['bmi']
df['mynewfeaturec1'] = df['mynewfeaturec1'] > 1600
df['mynewfeaturec2'] = df['age'] * df['bmi']
df['mynewfeaturec2'] = df['mynewfeaturec2'] > 1800
df['mynewfeaturec3'] = df['age'] * df['bmi']
df['mynewfeaturec3'] = df['mynewfeaturec3'] > 1690
df['mynewfeaturec4'] = df['age'] * df['bmi']
df['mynewfeaturec4'] = df['mynewfeaturec4'] > 1710
df['mynewfeaturec5'] = df['age'] * df['bmi']
df['mynewfeaturec5'] = df['mynewfeaturec5'] > 1700


df['mynewfeatured'] = df['age'] * df['bmi']
df['mynewfeaturee'] = df['age'] + df['bmi']


print('mynewfeature1', df['mynewfeature1'].corr( df['diabetes'] )) 
print('mynewfeature3', df['mynewfeature3'].corr( df['diabetes'] )) 


print('mynewfeaturec1', df['mynewfeaturec1'].corr( df['diabetes'] )) 
print('mynewfeaturec2', df['mynewfeaturec2'].corr( df['diabetes'] )) 
print('mynewfeaturec3', df['mynewfeaturec3'].corr( df['diabetes'] )) 
print('mynewfeaturec4', df['mynewfeaturec4'].corr( df['diabetes'] )) 
print('mynewfeaturec5', df['mynewfeaturec5'].corr( df['diabetes'] )) 

print('mynewfeatured', df['mynewfeatured'].corr( df['diabetes'] )) 
print('mynewfeaturee', df['mynewfeaturee'].corr( df['diabetes'] )) 


df = df.dropna()
for c in df.select_dtypes(exclude = ['object']):
	df[c] = df[c].astype(int)
	df[c] = (df[c]- df[c].min()) / (df[c].max() - df[c].min())

df.to_csv("week6h.csv")


sys.exit(1)

df = df[ df['blood_glucose_level'] < 205 ]
df = df[ df['blood_glucose_level'] > 100 ]
df = df[ df['HbA1c_level'] < 6.8 ]
df = df[ df['bmi'] < 80 ]

df = df.sample(frac = 0.10)

# Compute the average target value for each pair of feature1 and feature2
grouped = df.groupby(['bmi', 'age'])['diabetes'].mean().reset_index()
# Scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(grouped['bmi'], grouped['age'], c=grouped['diabetes'], cmap='viridis')
plt.xlabel('bmi')
plt.ylabel('age')
plt.title('Scatter Plot of Feature 1 and Feature 2 with Average Target')
plt.colorbar(scatter, label='Average Target')
plt.grid(True)
plt.show()
