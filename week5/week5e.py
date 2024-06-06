import sys
f = "week5_House Price India.csv"

import pandas as pd
import matplotlib.pyplot as plt
"""
df = pd.read_csv(f)

print(df.corr())


plt.scatter( df['condition of the house'], df['Built Year'] )

plt.show()
"""

f = "week5_coffee.csv"
df = pd.read_csv(f)






df = df[ df['Size'] != 'Not Defined' ]
df = df[ df['product_category'] != 'Flavours' ]

# .str.contains: bu ifadeyi iceriyor mu, does the text contains the given
# ~ ==> NOT
df = df[ ~df['product_detail'].str.contains('shot') ]
df = df[ ~df['product_detail'].str.contains('Chai') ]

print( df['product_category'].value_counts(normalize = True) )

#: Conversion to date type
print(df.dtypes)
df['transaction_date'] = pd.to_datetime(df['transaction_date'], format = "%d-%m-%Y")
print(df.dtypes)
# 01-01-2023
print(df)

#: After we have changed into "date", we have a new special property

df['Month'] = df['transaction_date'].dt.month
df['WeekDay'] = df['transaction_date'].dt.weekday

# 0 = Monday
# 1 = Tuesday
# ...
# 5 = Saturday
# 6 = Sunday

# isin( [] ) # bunlardan biri mi? is one of the values
df['Weekend'] = df['WeekDay'].isin( [5, 6] )

# convert into numeric
df['Weekend'] = df['Weekend'].astype(int)

weekends = df[ df['Weekend'] == 1 ]
nonweekends = df[ df['Weekend'] == 0 ]

print(len(weekends) / 2 )
print(len(nonweekends) / 5)

print(df)


print( df.groupby(by = ['Month'] ).size() )


df['transaction_time'] = pd.to_datetime( df['transaction_time'], format='%H:%M:%S' )
df['Hour'] = df['transaction_time'].dt.hour


print( df.groupby(by = ['Hour'] ).size() )

# 06:00
# ...
# 20:00

# vakit
vakit = {
	6: 'morning',
	7: 'morning',
	8: 'morning',
	9: 'morning',
	10: 'morning',
	11: 'noon',
	12: 'noon',
	13: 'noon',
	14: 'afternoon',
	15: 'afternoon',
	16: 'afternoon',
	17: 'before-evening',
	18: 'before-evening',
	19: 'evening',
	20: 'evening',
}


# map = [match something with something]
df['Vakit'] = df['Hour'].map( vakit )
# df.to_csv("week5e.csv", index = False)
print(df)


print( df.groupby(by = ['Vakit'] ).size() )


da = pd.DataFrame(df.groupby( by = ['Hour', 'Month'] ).size())
da.to_csv("week5e-da.csv")
print( da )



print( df.groupby( by = ['store_location', 'product_category']).size() )



#plt.scatter( df['transaction_qty'], df['unit_price']  )
#plt.show()

	

print( df['product_detail'].value_counts() )


products = list(df['product_detail'].unique())

data = {}

for p in products:
	data[p] = df[ df['product_detail'] == p]
	data[p] = data[p].groupby( by = ['Month'] ).size().values 


print(data)
# method 1:
#latte = df[ df['product_detail'] == 'Latte']
#latte = latte.groupby( by = ['Month'] ).size().values
#cappuccino = df[ df['product_detail'] == 'Cappuccino' ]
#cappuccino = cappuccino.groupby( by = ['Month'] ).size().values
#plt.plot( latte, label = 'Latte' )
#plt.plot( cappuccino, label = 'Cappuccino' )



for p in products:
	plt.plot( data[p], label = p )

plt.legend()
plt.show()




sizes = dict(df['Size'].value_counts())
plt.pie(sizes.values(), labels=sizes.keys())
plt.show()




# NO MEANING
df.dropna()

# Explanation
# Drop the none(nulls, nas) of the dataframe, and overwrite it into itself
df = df.dropna() # RETURN ME A NEW DATAFRAME, KEEP THE ORIGINAL UNTOUCHED!

# Update the original!!!!
df.dropna(inplace = True)






#When inplace=True is passed, the data is renamed in place (it returns nothing), so you'd use:
#df.an_operation(inplace=True)

#When inplace=False is passed (this is the default value, so isn't necessary), performs the operation and returns a copy of the object, so you'd use:
#df = df.an_operation() 







