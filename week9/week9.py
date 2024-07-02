import sys
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("week8_patient_dataset.csv")
target = "hospital_death"
"""
df['age>40'] = df['age'] > 50
print(df['age>40'].corr(df[target]))
datax = []
datay = []
for i in range(int(df['age'].min()), int(df['age'].max() + 1)):
	datax.append(i)
	datay.append( df[ df['age'] == i ][target].mean() )
plt.plot(datax, datay)
plt.show()
"""

df['weightZ'] = (df['weight'] - df['weight'].mean()) / df['weight'].std()
df['heightZ'] = (df['height'] - df['height'].mean()) / df['height'].std()

df['weightMM'] = (df['weight'] - df['weight'].min()) / (df['weight'].max() - df['weight'].min())
df['heightMM'] = (df['height'] - df['height'].min()) / (df['height'].max() - df['height'].min())

def anom1( row ):
	if row['weightZ'] > 2.4: return 1
	if row['heightZ'] > 2.4: return 1

	if row['weightZ'] < -1.8: return 1
	if row['heightZ'] < -1.8: return 1
	return 0

df['isanomaly1'] = df.apply(lambda row: anom1(row), axis = 1)

for i in [15,20,25,35,40,45,50,55,60,65,70,75,80,85]:
	df['yasli'] = df['age'] < i
	df['myfeature1'] = df['yasli'] + df['elective_surgery']
	print(i,'<', df['myfeature1'].corr(df[target]))

	df['yasli'] = df['age'] > i
	df['myfeature1'] = df['yasli'] + df['elective_surgery']
	print(i,'>', df['myfeature1'].corr(df[target]))




df['myfeature2'] = df['bmi'] > (df['bmi'].mean() + 2 * df['bmi'].std())
df['myfeature2'] = df['bmi'] * df['elective_surgery']
print(df['myfeature2'].corr(df[target]))


df_num = df.select_dtypes( exclude = ['object'])
for c in df_num:
	if c != target:
		df_num[c] = (df_num[c] - df_num[c].mean()) / df_num[c].std()



neg = []
pos = []

for c in df_num:
	if c != target:
		corr = df_num[ c ].corr(df[target])
		if corr > 0.1:
			pos.append(c)
		elif corr < 0.1:
			neg.append(c)


df['pos'] = df_num[ pos ].sum(axis = 1)
df['neg'] = df_num[ neg ].sum(axis = 1) 

print(df['pos'].corr(df[target]))
print(df['neg'].corr(df[target]))


problems = ['aids','cirrhosis','hepatic_failure','immunosuppression','leukemia','lymphoma','solid_tumor_with_metastasis']

corrs = {}
for p in problems:
	corrs[ p ] = df[p].corr(df[target])

df['myfeature4'] = df[problems].sum(axis = 1)
print('myfeature4', df['myfeature4'].corr(df[target]))



df['myfeature6'] = df['myfeature4'] > 1
print('myfeature6', df['myfeature6'].corr(df[target]))



def vur( row ):
	s = 0
	for p in problems:
		s += row[p] * corrs[p]
	return s

df['myfeature5'] = df.apply(lambda row: vur(row), axis = 1)
print( 'myfeature5', df['myfeature5'].corr(df[target]))

print(corrs)
df['myfeature3'] = df['apache_3j_bodysystem'] == df['apache_2_bodysystem']
print( 'myfeature3', df['myfeature3'].corr(df[target]))





df['potassium-range'] = df['d1_potassium_max'] - df['d1_potassium_min']
print('potassium-range', df['potassium-range'].corr(df[target]))
print('potassium-max', df['d1_potassium_max'].corr(df[target]))
print('potassium-min', df['d1_potassium_min'].corr(df[target]))


def x(row):

	return max(row['apache_4a_hospital_death_prob'], row['apache_4a_icu_death_prob'])
		

df['myfeature7'] = df.apply(lambda row: x(row), axis = 1)

print('apache_4a_hospital_death_prob', df['apache_4a_hospital_death_prob'].corr(df[target]))
print('apache_4a_icu_death_prob', df['apache_4a_icu_death_prob'].corr(df[target]))
print('myfeature7', df['myfeature7'].corr(df[target]))










sys.exit(1)
plt.hist( df['weightZ'], alpha = 0.5 )
plt.hist( df['heightZ'], alpha = 0.5 )
plt.show()



def ageKIRILIM( age ):
	if age < 41:
		return 0.035
	else:
		return 0.04 + ((0.15-0.04) / (91-41)) * (age - 41)


