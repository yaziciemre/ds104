import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json


f = "week7_ins_train.csv"
df = pd.read_csv(f)


#: Remove the id, which has no sense
del df['id']

#: Replace
df['Gender'] = df['Gender'].map({'Male':0,'Female':1})

#: Remove Driving_License
del df['Driving_License']

most = df['Region_Code'].mode()[0]
df['Popular_Region'] = df['Region_Code'] == most
df['Popular_Region'] = df['Popular_Region'].astype(int)
del df['Region_Code']

#: Replace
df['Vehicle_Damage'] = df['Vehicle_Damage'].map({'Yes': 1, 'No':0})

#: Replace, limit
def channel( value ):
	if value in [152,26,124,160]:
		return 'C' + str(value)
	else:
		return 'others'

df['Policy_Sales_Channel'] = df['Policy_Sales_Channel'].apply(channel)


df['AgeR1'] = df['Age'].apply(lambda value: value < 51 and value > 31)
df['AgeR1'] = df['AgeR1'].astype(int)

df['AgeR2'] = df['Age'].apply(lambda value: value < 59 and value > 50)
df['AgeR2'] = df['AgeR2'].astype(int)

df['AgeL'] = np.log(df['Age'])
df['AgeS'] = np.sqrt(df['Age'])

print(df['AgeR1'].corr(df['Response']))
print(df['AgeR2'].corr(df['Response']))
print(df['Age'].corr(df['Response']))
print(df['AgeL'].corr(df['Response']))
print(df['AgeS'].corr(df['Response']))


# print(df['Vehicle_Age'].value_counts(normalize=True))



def AgeLimiter( age ):
	if age < 25 and age > 19:
		return 0.04
	if age >= 25 and age <= 30:
		return 0.036 + (age - 25) * 0.093
	if age > 30 and age < 50:
		return 0.22
	if age > 75:
		return 0.05
	if age >= 50 and age <= 75:
		return 0.17 - 0.004 * (age - 50)

df['MyAge'] = df['Age'].apply(AgeLimiter)
print('MyAge', df['MyAge'].corr(df['Response']))
"""

dataF = {}
dataM = {}
for i in range(df['Age'].min()):
	dataM[i] = 0
	dataF[i] = 0

for i in range(df['Age'].min(), df['Age'].max()):
	dataM[i] = round(df[ df['Gender'] == 0 ][ df['Age'] == i ]['Response'].mean(), 3)
	dataF[i] = round(df[ df['Gender'] == 1 ][ df['Age'] == i ]['Response'].mean(), 3)



print(json.dumps(dataM,  indent=4))
print(json.dumps(dataF,  indent=4))

plt.plot(dataM.values())
plt.plot(dataF.values())

plt.show()

df.to_csv("week7_ins_train_out.csv")
"""

#print(df['Age'].value_counts().to_dict())
#df['Age'] = df['Age'].map( data ) # TARGET AVERAGE
#print("XXX", df['Age'].corr(df['Response']))


binaries = ['Gender', 'Previously_Insured', 'Vehicle_Damage', 'Popular_Region']


for c in itertools.combinations(binaries, 2):
	c0 = c[0]
	c1 = c[1]

	m00 = df[ (df[c0] == 0) & (df[c1] == 0) ]['Response']
	m10 = df[ (df[c0] == 1) & (df[c1] == 0) ]['Response']
	m01 = df[ (df[c0] == 0) & (df[c1] == 1) ]['Response']
	m11 = df[ (df[c0] == 1) & (df[c1] == 1) ]['Response']

	c00 = len(m00)
	c01 = len(m01)
	c10 = len(m10)
	c11 = len(m11)

	r00 = round(m00.mean(), 3)
	r01 = round(m01.mean(), 3)
	r10 = round(m10.mean(), 3)
	r11 = round(m11.mean(), 3)

	print({'c0': c0, 'c1': c1, 'c00': c00, 'r00': r00, 'c01': c01, 'r01': r01, 'c10': c10, 'r10': r10, 'c11': c11, 'r11': r11})


df['myfeature2'] = (df['Previously_Insured'] == 0) & (df['Vehicle_Damage'] == 1)
print('myfeature2', df['myfeature2'].corr(df['Response']))


print( df['Vehicle_Damage'].corr(df['Response']) )

print(df.select_dtypes(exclude = ['object']).corr())




# cok genel    ==> bad | 20-70 yas arasindakilerin response 0.20

# cok spesifik ==> bad | 21: 0.2, 22: 0.3, .......
# ==> PROBLEM ==> DATA OVERFITTING


scalars = ['Annual_Premium', 'Vintage']

for s in scalars:
	print('scalar', s, df[s].corr(df['Response']))
	
	df['x'] = df[ s ] > df[s].mean()
	print('x>mean', df['x'].corr(df['Response']))

	df['x'] = df[ s ] > df[s].quantile(0.75)
	print('x>q3', df['x'].corr(df['Response']))

	df['x'] = df[ s ] > df[s].quantile(0.60)
	print('x>q60', df['x'].corr(df['Response']))


	df['x'] = np.log(df[s])
	print('log', df['x'].corr(df['Response']))

	df['x'] = np.sqrt(df[s])
	print('sqrt', df['x'].corr(df['Response']))

	df['x'] = np.power(df[s], 0.1)
	print('p01', df['x'].corr(df['Response']))

	df['x'] = np.power(df[s], 2.0)
	print('p20', df['x'].corr(df['Response']))


print(df['Annual_Premium'].describe())

df = df[ df['Annual_Premium'] < df['Annual_Premium'].quantile(0.99) ]
df = df[ df['Annual_Premium'] > 10004 ]

df['Annual_Premium'] = df['Annual_Premium'] / 1000
df['Annual_Premium'] = df['Annual_Premium'].astype(int)

data = {}
for i in range(df['Vintage'].min()):
	data[i] = 0

for i in range(df['Vintage'].min(), df['Vintage'].max()):
	data[i] = round(df[ df['Vintage'] == i ]['Response'].mean(), 3)

plt.plot(data.values())

plt.show()


def AP( value ):
	if value < 12:
		return 0.0
	step = (0.175 - 0.075) / 60.0
	return 0.075 + (value - 10) * step

df['AP'] = df['Annual_Premium'].apply(AP)
print(df['AP'].corr(df['Response']))




for v in df['Vehicle_Age'].unique():
	for p in df['Policy_Sales_Channel'].unique():
		sub = df[ (df['Vehicle_Age'] == v) & (df['Policy_Sales_Channel'] == p) ]
		
		print(v, p, len(sub), sub['Response'].mean())

"""


"""