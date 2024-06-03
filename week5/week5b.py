

file = "week4_Invistico_Airline.csv"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(file)

print(df)

# I want to do some mathematical operations
# So that I want to SELECT ONLY THE NUMERICS
print(df.dtypes.to_dict())

print( df.select_dtypes(exclude = ['object']) ) # discard
print( df.select_dtypes(include = ['int64', 'float64']) )

# df[ ['Age', 'Flight Distance', 'Seat comfort', '.....'] ]

numerics = df.select_dtypes(exclude = ['object'])
nonnumerics = df.select_dtypes(include = ['object'])
print('===============')
print('numerics')
print(numerics)
print('nonnumerics')
print(nonnumerics)


# 4 different ways to do same thing!
# numerics = df.select_dtypes(include = ['number']) == int64, float64
#if pd.api.types.is_numeric_dtype(df[column]): 
#if df[column].dtype == np.float64 or df[column].dtype == np.int64:
# if str(df[column].dtype) == 'int64'

# WHAT ARE OUR CAPABILITIES = EVERYTHING


# integer_or_float = r"^\-?[0-9]+(\.[0-9]+)?$"
# REGEX COSTLY, PAHALI


# 1 column
# 2 columns
# 3 list of sart

# list of sartlar
print( df[ df['Customer Type'].isnull() ] )
print( df[ df['Customer Type'].notnull() ] )
# SELECT * FROM TABLE WHERE CustomerType is NOT NULL

for c in df.columns:  # . ==> nin nun DF'nin kolonlari
	print(c, df[c].isnull().sum())

print('===================')
null_counts = df.isnull().sum() # Sums the trues/falses for each column
print(null_counts.to_dict())




# df.isnull().sum().to_dict()
# df in, null olup olmamasi durumumun, sumlarini, dictionary'ye transform donustur, cevir


print(df.isnull().sum().to_dict())

# Nulls will be explained later on.


# conda install openpyxl - windows
# pip3 install openpyxl  - unix / mac

filename = 'week5test.xlsx'
df0 = pd.read_excel(filename, 'Sheet2')
print(df0)

#: Read the excel file to see the names of the sheets
xl = pd.ExcelFile(filename)
print(xl.sheet_names)  # see all sheet names
dfx = xl.parse('Sheet1')  # read a specific sheet to DataFrame
dfx = pd.read_excel( filename, xl.sheet_names[1])

# SELECT * FROM students
# SELECT * FROM grades
# SELECT * FROM lectures


# ==================================
# To use mode, at '.iloc[0]' at to the end
print( df['Gender'].mode().iloc[0] )
print( df['Gender'].mode()[0] )


# ===============
# To get the number of rows of a dataframe we can use one of the following
len(df)
df.shape[0]
df.count()

# =============
# Load a different file
df = pd.read_csv("week5_hotel_bookings.csv")
print(df)

# Show me, how much hotels customers from which country


print( df['country'].value_counts().to_dict() )

for c in df.columns:
	print(c)
	print(df[c].value_counts())






import matplotlib.pyplot as plt
total = df['country'].value_counts().values.sum()

def fmt(x):
    return '{:.1f}%\n{:.0f}'.format(x, total*x/100)

countries = df['country'].value_counts()
dictionary = countries.to_dict()


new_dictionary = {}
other = 0
for country in dictionary:
	if dictionary[country] > 2000:
		new_dictionary[ country ] = dictionary[ country ]
	else:
		other += dictionary[ country ]
new_dictionary['all other'] = other


plt.pie(new_dictionary.values(), labels=new_dictionary.keys())

plt.show()


# %10' un altindakileri ==> other



def pieChartOther( df column: str, percentage: float ):
	....




pieChartOther( df, 'country', 0.15 )
pieChartOther( df, 'country', 0.20 )

