
file = "week4_Invistico_Airline.csv"
file = "week5_hotel_bookings.csv"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(file)

print("df.shape [0]", df.shape)

# 17| To see which types of data the columns have
print( df.dtypes )

del df['company']
print(df.isnull().sum())

# Revisited
# Drops the columns which has a "nan" "None"
df = df.dropna()
print("df.shape [0a]", df.shape)
# 18| Values
# print( df['Gender'].values )


# 19| Unique
# SELECT DISTINCT [c] FROM TABLE
for c in df.select_dtypes(include=['object']).columns:
	if df[c].nunique() < 10:
		print( c, df[c].unique() )
	else:
		print( c, "There are too many values", df[c].nunique())


# hotel ['Resort Hotel' 'City Hotel']

# 20| New column
df['hotel_isResort'] = (df['hotel'] == 'Resort Hotel')

# 21| Delete a column
# del df['hotel']
df = df.drop(['hotel'], axis = 1)

# 22| astype, converts it into integer
df['hotel_isResort'] = df['hotel_isResort'].astype(int)

print(df)

print(df.dtypes)

# 23| Clip, clips / cuts the data between two ranges
# 85+ ==> 85
print("df.shape [1]", df.shape)

print(df['lead_time'].describe())
df['lead_time'] = df['lead_time'].clip(0, 300)
print(df['lead_time'].describe())

df = df.drop_duplicates()

print("df.shape [2]", df.shape)

# 24| Aging(!)
# Bring me the records which are later than 2015
# SELECT * FROM TABLE WHERE arrival_date_year > 2015
df = df[ df['arrival_date_year'] > 2015 ]

# 25| Saving
df.to_csv( "week5c.csv", index = False )
