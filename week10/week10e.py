
s = "week6_car_prices.csv"
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
t = 'sellingprice'
df = pd.read_csv(s, on_bad_lines='skip')

df = df[ df[t] < 50000 ]
df = df[ df[t] > 1500]

df[t] = (df[t] / 1000).astype(int)

#: Transform some features
df['transmission'] = df['transmission'].fillna('automatic')
df['transmission'] = df['transmission'].map({'manual': 0, 'automatic': 1})
df['condition'] = df['condition'].fillna(2.5)

#: Delete unnecessary
del df['saledate']
del df['seller']
del df['mmr']
del df['vin']

#: Transform
df['year'] = 2015 - df['year']
df['isnew'] = (df['year'] == 0).astype(int)
df['used'] = (df['odometer'] > 10).astype(int)

#: Downcast
df['body'] = df['body'].str.lower()
body = list(df['body'].unique())
body_map = {}
for b in body:
	body_map[b] = b
	if 'sedan' in str(b):
		body_map[b] = 'sedan'
	if 'wagon' in str(b):
		body_map[b] = 'wagon'
	if 'coupe' in str(b):
		body_map[b] = 'coupe'
	if 'van' in str(b):
		body_map[b] = 'van'
	if 'cab' in str(b):
		body_map[b] = 'cab'

df['body'] = df['body'].map(body_map)

#: Make dummy
df = pd.get_dummies( df, columns = ['body'])
for c in df.columns:
	if 'body' in c:
		df[c] = df[c].astype(int)

#: Make target average
make_price = df.groupby('make')['sellingprice'].mean().to_dict()
df['make'] = df['make'].map(make_price)



df = df.select_dtypes(exclude = ['object'])
df = df.dropna()
df = df.sample(frac = 0.2)


#: Target replacement!!!
#avg = df[t].mean()
#df[t] = df[t] - avg
#plt.hist(df[t])
#plt.show()


#part_a = df[ df['odometer'] < 300000 ] # car age < 2
#part_b = df[ df['odometer'] >= 300000 ]

y = df[t]
x = df.drop(columns = [t])
# reg = LinearRegression()
reg = RandomForestRegressor(max_depth=4, random_state=0)

reg.fit( x, y )

x['pred'] = reg.predict(x)
x['pred'] = x['pred'].astype(int)
x['pred'] = x['pred'].round(-1)
x['real'] = y
x['error'] = x['pred'] - x['real']
x['abs-error'] = x['error'].abs()
x['percentage'] = x['abs-error'] / x['real']



neg = x[ x['error'] < -1000 ]
pos = x[ x['error'] > 1000 ]


print(neg.drop(columns = ['error','abs-error','percentage', 'real', 'pred']).describe().round(3))
print(pos.drop(columns = ['error','abs-error','percentage', 'real', 'pred']).describe().round(3))



x.to_csv("week10e_output.csv")

print("ROWS", len(x))
print("CORR", x['pred'].corr(x['real']))
print( "MAE", x['abs-error'].mean() )
# MAE = mean absolute error
 
print("MAPE",x['percentage'].mean())
# MAPE = mean absolute percentage error

# MSE = mean square error
x['square'] = x['error'] * x['error']
print('MSE', x['square'].mean())

from sklearn.metrics import r2_score
print("R2", r2_score( x['real'], x['pred'] ))
#weighted_accuracy.append( r2_score( x['real'], x['pred'] ) * len(x) )

print('============')


#print(np.sum(weighted_accuracy) / len(df))


"""
CORR 0.7874546865219796
MAE 3740.4357528413207
MAPE 0.3659569664376079
MSE 27277951.439991888
R2 0.61988222574485

"""