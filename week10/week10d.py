from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
s = "realtor-data.zip.csv"
import pandas as pd
t = 'price'
df = pd.read_csv(s)
del df['status']
del df['city']
del df['zip_code']
del df['street']
del df['brokered_by']

state_price = df.groupby(by = ['state'])[t].mean().to_dict()
df['state'] = df['state'].map(state_price)

df['prev_sold_date'] = df['prev_sold_date'].isnull().astype(int)

df = df.dropna()
print(df)
df = df[ df[t] > 100000 ]

y = df[t]
x = df.drop(columns = [t])
# reg = LinearRegression()
reg = RandomForestRegressor(max_depth=4, random_state=0)

reg.fit( x, y )

x['pred'] = reg.predict(x)
x['real'] = y
x['error'] = x['pred'] - x['real']

x['abs-error'] = x['error'].abs()
x['percentage'] = x['abs-error'] / x['real']
print(x)


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

"""
print(x['pred'].corr(x['real']))
x = x.sample(frac = 0.01)
x = x[ x['pred'] < x['pred'].quantile(0.95) ]
x = x[ x['real'] < x['real'].quantile(0.95) ]

x = x[ x['pred'] > x['pred'].quantile(0.05) ]
x = x[ x['real'] > x['real'].quantile(0.05) ]


plt.scatter( x['pred'], x['real'] )
plt.show()
"""