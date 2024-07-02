
s = "week9_loan_Training Data.csv"
import pandas as pd
df = pd.read_csv(s)

half = int(len(df) / 2)
dfa = df.head(half)
dfb = df.tail(half)

print('UNKNOWN')
print(dfa.describe())
print(dfb.describe())
print('====================')

df = df.sample(frac = 1.0)
dfa = df.head(half)
dfb = df.tail(half)
print('TIME-INDEPENDED')
print(dfa.describe())
print(dfb.describe())

#: Data aging
L = int(len(df) / 5)

a = df.iloc[L*0:L*1]
b = df.iloc[L*1:L*2]
c = df.iloc[L*2:L*3]
d = df.iloc[L*3:L*4]
e = df.iloc[L*4:L*5]

a = a.sample(frac = 0.2)
b = b.sample(frac = 0.4)
c = c.sample(frac = 0.6)
d = d.sample(frac = 0.8)

df = pd.concat( [a,b,c,d,e] )
df = df.sample(frac = 1.0)

del df['Id']

df['Car_Ownership'] = df['Car_Ownership'].map({'yes': 1, 'no': 0})
df['Married/Single'] = df['Married/Single'].map({'single': 0, 'married': 1})


city_state = {}
for s in df['STATE'].unique():
	cities = list(df[ df['STATE'] == s ][ 'CITY' ].unique())

	for c in cities:
		city_state[ c ] = s



for c in df['CITY'].unique():
	
	city_belongs_to_state = df[ df['CITY'] == c ]['STATE'].unique()
	if len(city_belongs_to_state) > 1:
		print("PROBLEM", c, city_belongs_to_state)

df['WhatAgeStartedWorking'] = df['Age'] - df['Experience']

df['SingleWork'] = df['Experience'] == df['CURRENT_JOB_YRS']
df['LastWorkRatio'] = df['CURRENT_JOB_YRS'] / df['Experience'] 
df['SinceWhatAgeIsWorking'] = df['Age'] - df['CURRENT_JOB_YRS']

uni = [
    "Web_designer",
    "Comedian",
    "Fashion_Designer",
    "Drafter",
    "Flight_attendant",
    "Technical_writer",
    "Hotel_Manager",
    "Graphic_Designer",
    "Police_officer",
    "Secretary",
    "Politician",
    "Computer_operator",
    "Technician",
    "Artist",
    "Consultant",
    "Aviator",
    "Army_officer",
    "Chef",
    "Designer",
    "Firefighter",
    "Civil_servant",
    "Official"
]

df['uni'] = df['Profession'].isin( uni )
df['Income'] = df['Income'] / 1000
df['Income'] = df['Income'].astype(int)

#df['Enough'] = df.apply(lambda row: row['Experience'] > 5 and df['CURRENT_JOB_YRS'] > 3, axis = 1)


print(df['WhatAgeStartedWorking'].describe())

print(list(df['Profession'].value_counts().to_dict().keys()))


import matplotlib.pyplot as plt

sub = df.sample(frac = 0.05)
plt.scatter( sub['Income'], sub['Age'] )
plt.show()
