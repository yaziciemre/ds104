
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("week7_patient_dataset.csv")
print(df['hospital_id'].value_counts())

T = 'hospital_death'

df = df.dropna()
"""
column = 'bmi'
df[column] = df[column].astype(int)
data = {}
for i in range(df[column].min()):
	data[i] = 0
for a in range(df[column].min(), df[column].max()):
	data[a] = df[ df[column] == a ][ T ].mean()


plt.plot(data.values())

plt.show()
"""

print( df.groupby(['apache_3j_bodysystem'])[T].mean() )




