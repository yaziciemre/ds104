

# If they are in same folder, we do not need to use full path
# week4e.py
# week4_Invistico_Airline.csv

# In case of you want to use full path use "r" at the begining
"""
# file = "c:\\users\\emre\\downloads\\newfile.csv"
"""
file = "week4_Invistico_Airline.csv"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 00|read_csv:  Load the data in file into a variable called df (dataframe)
df = pd.read_csv(file)

# 01|len: Length of data frame in rows!!
print(len(df))

# 02|shape: Rows, columns in dataframe
print(df.shape)

# 03|columns: Columns
print(df.columns) # attribute

# 04|info: Information about columns
print(df.info()) # fonksiyon method

# object == str
# non-null = there is no item with value "none", all filled
# In some cases there are some columns with null values!
# We will learn how to fill them up

# 05|describe: Statistical information about columns
print(df.describe()) # method

# 06|sample: Take a smaller fraction of dataset
# df = df.sample(frac = 0.5) # 50 faizini al (randomly)
# df = df.sample(n = 5000) # 5000 tane row al (randomly)
# If the dataset is very large, we may need to narrow it down
# Because other operations will take too long time to process

# df = df.sample(n = 100) # Those modifier(!) functions returns a new dataframe
#                         # So we overwrite the original one

# 07|drop_duplicates: Drops the same rows
print("BEFORE", len(df))
df = df.drop_duplicates()
print("AFTER", len(df))
# If the dataset contains duplicate rows, we may need to delete them

# VERY DANGEROUS, NEED TO BE CAREFUL
df.drop_duplicates( subset = ['Age','Type of Travel','Class'] )

# 08|drop: Drop the columns (or rows, but later)
print("BEFORE", df.columns)
df = df.drop( 'Seat comfort', axis = 1 ) # axis = 1 (column)
print("AFTER", df.columns)
# In some cases, we discard some columns. We will not be using some of the columns
# Unique values

# 09|: Get some part of the database (as a range)

l = ['Ahmet', 'Mehmet', 'Anar', 'Suleyman', 'Mustafa']
# l[0:]

print(df[:10])
print(df[100:600])

# First, 1000 rows
print(df.head(1000).describe())

# Last, 1000 rows
print(df.tail(1000).describe())


# IMPORTANT, 
# L = last 1000 items, bitis, end
# F = first 1000 items, baslangic, begin

# What does |L-F| give us as information?

# 10| iloc: Accessing a single row

r = df.iloc[ 110 ]  # integer location
print("row number 110", r)
print("row as dict",  r.to_dict())

# 11| dropna: Bos olanlari sil
print("BEFORE", df.shape)
# df = df.dropna()

# delete the rows, where their flight distance is null or Arrival Delay in Minutes is null
df = df.dropna(subset = ['Flight Distance', 'Arrival Delay in Minutes'])
df = df.dropna(subset = ['Arrival Delay in Minutes', 'Flight Distance'])
# ANY OF THESE COLUMNS IF EMPTY, THEN, DELETE THE ROW COMPLETELY

print("AFTER", df.shape)

# 12| sort_values: Sort the dataframe by columns
#df = df.sort_values( by = ['Arrival Delay in Minutes'])
#df = df.sort_values( by = ['Arrival Delay in Minutes'] , ascending=[False])
print(df)

# 13| Filtering
customers_who_waits_more_than_1_hour = df.query("`Arrival Delay in Minutes` < 15")
# "SELECT * FROM flights WHERE ArrivalDelayInMinutes < 15"
print(customers_who_waits_more_than_1_hour)


# use of [] in python
# 1--> dictionary item  a = {'x': 3, 'y':4},         a['x'']
# 2--> list item        a = ['x','y','z']            a[2]


# use of [] in pandas
# 1--> sart, condition, kosul, statement, if: FILTERING, WHERE
cwwmt1h = df[ df['Arrival Delay in Minutes'] < 15 ]
#             |---------------------------------| sart

# 2--> a string (name of column)
print(df['Age'])


# 3--> a list of strings (names of the columns)
s = df[ ['Age', 'Gender'] ]
#       |---------------|   -> a list of strings
# SELECT Age, Gender FROM table

# df.query( 'Age < 60 & Age > 20' )
# df[ (df['Age'] > 20) & (df['Age'] < 60) ]

a = df[ df['Age'] < 60 ]
a = a[ a['Age'] > 20 ]

# COMPLEX, DO NOT USE: df[ df['Age'] < 60 ][ df['Age'] > 20 ]

# It excludes the nulls in filter
print( len(df['Age']))
print( len(df[ 'Age' ].dropna()) )
print( len(df[df['Age'] < 60]))
print( len(df.dropna(subset=['Age'])[df['Age'] < 60]))

# Before filtering, we may need to store the ones which has nulls.


print( df['Age'].max() )
print( df['Age'].min() )
print( df['Age'].mean() )
print( df['Age'].std() )
print( df['Age'].kurt() )
print( df['Age'].skew() )
print( df['Age'].mode() )
print( df['Age'].median() )
print( df['Age'].quantile(0.25) )
print( df['Age'].quantile(0.75) )


"""
# A code to remove outlier columns for "Age" only
q1 = df['Age'].quantile(0.25)
q3 = df['Age'].quantile(0.75)
iqr = q3-q1
df = df[ df['Age'] < q3 + 1.5 * iqr ]
df = df[ df['Age'] > q1 - 1.5 * iqr ]


q1 = df['Flight Distance'].quantile(0.25)
q3 = df['Flight Distance'].quantile(0.75)
iqr = q3-q1
df = df[ df['Flight Distance'] < q3 + 1.5 * iqr ]
df = df[ df['Flight Distance'] > q1 - 1.5 * iqr ]
# if operation is same, but the parameter is different, use a function (def)
"""


def excludeOutliers( df, column ):
	q1 = df[column].quantile(0.25) # 1. quartile
	q3 = df[column].quantile(0.75) # 3. quartile
	iqr = q3-q1
	df = df[ df[column] < q3 + 1.5 * iqr ]
	df = df[ df[column] > q1 - 1.5 * iqr ]
	return df

def countNofOutliers( df, column ):
	q1 = df[column].quantile(0.25) # 1. quartile
	q3 = df[column].quantile(0.75) # 3. quartile
	iqr = q3-q1

	da = df[ df[column] < q3 + 1.5 * iqr ]
	da = da[ da[column] > q1 - 1.5 * iqr ]
	return len(df) - len(da)


print( "Age", countNofOutliers( df, 'Age' ) )
print( "Flight Distance", countNofOutliers( df, 'Flight Distance' ) )
print( "Arrival Delay in Minutes", countNofOutliers( df, 'Arrival Delay in Minutes' ) )
print( "Departure Delay in Minutes", countNofOutliers( df, 'Departure Delay in Minutes' ) )

# Exp : 
# 16 yasli bireyin tek olarak outlier degil , 
# evlilik sayi columnla kiyasda 

# 3 kez evlenmesi gibi bir sheyde outliermi sayiliyor?

# Anar => 16 
# Univeristy (min age) ==> 18 [regulation] government
# Univeristy talebeler = 18, 18, 19, 19, 19, 19, 19, 20, 21,22,24

# Data preprocessing
# Data cleaning


# 14| Creating a new column

q1 = df['Arrival Delay in Minutes'].quantile(0.25) # 1. quartile
q3 = df['Arrival Delay in Minutes'].quantile(0.75) # 3. quartile
iqr = q3-q1
upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr
df['IsArrivalOutlier'] = (df['Arrival Delay in Minutes'] > upper) | (df['Arrival Delay in Minutes'] < lower)



q1 = df['Departure Delay in Minutes'].quantile(0.25) # 1. quartile
q3 = df['Departure Delay in Minutes'].quantile(0.75) # 3. quartile
iqr = q3-q1
upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr
df['IsDepartureOutlier'] = (df['Departure Delay in Minutes'] > upper) | (df['Departure Delay in Minutes'] < lower)

# | ==> veya or 
print(df)


print( df[ (df['IsDepartureOutlier'] == True) & (df['IsArrivalOutlier'] == False	) ] )




talebe_bal = 80
gecis_skor = 70

# variable      = "SART"   (true/false)
talebe_gecti_mi = talebe_bal > gecis_skor
print(talebe_gecti_mi)


"""
# sys.exit(0) # sys.exit => sistem den cik (quit), error code = 1
print("BEFORE")
print(df[ ['Age', 'Flight Distance'] ].describe())

before = df.copy()

df = excludeOutliers( df, 'Age' )
df = excludeOutliers( df, 'Flight Distance' )
print("AFTER")
print(df[ ['Age', 'Flight Distance'] ].describe())


plt.hist(before['Flight Distance'])
plt.hist(df['Flight Distance'])
plt.show()
"""





