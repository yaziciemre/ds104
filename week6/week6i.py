import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("week6_car_prices.csv", on_bad_lines='skip')

df['year2015'] = df['year'] == 2015
print(df)

print( df['sellingprice'].corr(df['year']) )
print( df['sellingprice'].corr(df['year2015']) )


state_price = df.groupby('state')['sellingprice'].mean().to_dict()
print(state_price)

# Create an empty dataframe with 2 columns
new_df = pd.DataFrame( columns = ['state', 'meanprice'])
print('===========')
print(new_df)
print('===========')

for i in state_price:
	print("len(new_df)", len(new_df), [ i, state_price[i] ])
	# Which row to be assigned
	new_df.loc[ len(new_df) ] = [ i, state_price[i] ] # new row adding

new_df.to_csv("week6f_newdf.csv")

def statePriceFunction( state: str ) -> int:
	if state in ['nm','ma','ok','md','va','nc','al','pr']:
		return 7900
	if state in ['ns','sc','la','in','ab','ms','ny','az','or','ut','hi','ne','ga']:
		return 11500
	#....



# df['statePrice'] = df['state'].apply( statePriceFunction )


print(df['color'].unique())


def getDummies( df, column ):

	for c in df[column].unique():
		df[column + '_' + c] = (df[column] == c)
	del df[column]
	return df


# df = pd.getDummies( df, ['color'] )
print('===============')
print( pd.get_dummies( df, columns = ['make'] ).columns )
print( pd.get_dummies( df, columns = ['color'] ).columns )




print( df['odometer'].corr(df['sellingprice']) )



df['fark'] = df['sellingprice'] - df['mmr']

df['conditionX'] = df['condition'] >= 3.5
print(df['conditionX'].corr(df['fark']))

print(df['condition'].corr(df['sellingprice']))

#print( df.select_dtypes(exclude = ['object']).corr()['fark'] )

xs = []
ys = []
for i in df['condition'].unique():
	xs.append( i )
	ys.append( df[ df['condition'] == i ]['sellingprice'].mean() )


#plt.scatter( xs, ys )
#plt.show()

#df_res['DateTime'] = pd.to_datetime(df_res['DateTime'], utc=True)

df['saledate'] = pd.to_datetime(df['saledate'], utc=True)
df['month'] = df['saledate'].dt.month


print(df['month'].corr( df['sellingprice'] ))
print(df.dtypes)

print( df.groupby('month')['sellingprice'].mean() )

# DAY_NUMBER   15/02/2020
# WEEK_NUMBER
# YEAR


