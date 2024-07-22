
# polars!
import sys
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("week12_AEP_hourly.csv")
df = df[-24*365*2:].reset_index() # last 2 years (2 x year(365) x 24)
del df['index']


#plt.plot(df['AEP_MW'])
#plt.show()

def linreg(X, Y):
    """
    return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
    """
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det


x = list(df['AEP_MW'].values)
m, n = linreg(range(len(x)),x) 

print(m, n)




for c in [6, 12, 18, 24,24*7]:
	df[f'lag{c}'] = df['AEP_MW'].shift(c)

df['trend'] = [n + m * i for i in range(len(df))]
df['Datetime'] = pd.to_datetime( df['Datetime'] )
df['day'] = df['Datetime'].dt.day
df['month'] = df['Datetime'].dt.month
df['weekday'] = df['Datetime'].dt.weekday
df['weekend'] = df['weekday'].isin([5,6]).astype(int)
df['hour'] = df['Datetime'].dt.hour


df['specialseason'] = df['month'].isin([12,1,2,6,7,8]).astype(int)
print('specialseason', df['specialseason'].corr( df['AEP_MW'] ))

df['month:hour'] = df.apply(lambda row: str(row['month']) + '_' + str(row['hour']), axis = 1)


for c in ['day', 'month', 'weekday', 'weekend', 'hour', 'month:hour']:
	cat = df.groupby(c)['AEP_MW'].mean().to_dict()
	df[f'cat_{c}'] = df[c].map(cat)
	print( c, df[f'cat_{c}'].corr(df['AEP_MW']) )


df['CH'] = df['month'].isin([10,11,12,1,2,3]).astype(int)

cat = df.groupby('month:hour')['AEP_MW'].mean().to_dict()
df['month:hour'] = df['month:hour'].map(cat)
df['AEP_MW2'] = df['AEP_MW'] - df['month:hour']





# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2016, 1, 1)
end = datetime(2018, 8, 3)

# Create Point for Vancouver, BC
location = Point(40.12728, -76.13772)

# Get daily data for 2018
data = Daily(location, start, end)
data = data.fetch()

#print(data)
# Plot line chart including average, minimum and maximum temperature
#data.plot(y=['tavg'])
#plt.show()
data = data.reset_index()
data['time'] = data['time'].astype(str)
data = dict(zip(data['time'], data['tavg']))

def findTemp( incomingdate ):
	incomingdate = str(incomingdate).split(" ")[0]
	return data[ incomingdate ]

df['Temperature'] = df['Datetime'].apply( findTemp )

print(df)
sys.exit(1)

print(df['Datetime'].describe())

plt.plot(df['AEP_MW'])
plt.plot(df['AEP_MW2'])
plt.show()




