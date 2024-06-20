
"""
f = "week7_train_fare.csv"
import pandas as pd
df = pd.read_csv(f)
df = df.sample(frac = 0.15)
df.to_csv("week7_train_fare_small.csv")
"""
import matplotlib.pyplot as plt
import sys
import math
f = "week7_train_fare_small.csv"
import pandas as pd
df = pd.read_csv(f)


# mostly, taking the "static/constant" part of the target, works fine!!
df['fare_amount'] = df['fare_amount'] - 3.3


timeMap = {
	0: 'night',
	1: 'night',
	2: 'night',
	3: 'night',
	4: 'night',
	5: 'night',
	6: 'night',
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
	17: 'afternoon',
	18: 'evening',
	19: 'evening',
	20: 'evening',
	21: 'evening',
	22: 'night',
	23: 'night',
}


seasonMap = {
	1: 'winter',
	2: 'winter',
	3: 'spring',
	4: 'spring',
	5: 'spring',
	6: 'summer',
	7: 'summer',
	8: 'summer',
	9: 'autumn',
	10: 'autumn',
	11: 'autumn',
	12: 'winter',

}


df['time'] = df['hour'].map( timeMap )
df['season'] = df['month'].map( seasonMap )

def euclidean( row ):
	x1 = row['pickup_longitude']
	y1 = row['pickup_latitude']

	x2 = row['dropoff_longitude']
	y2 = row['dropoff_latitude']

	return math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )


def euclideanX( row ):
	x1 = row['pickup_longitude']
	x2 = row['dropoff_longitude']
	return abs(x1-x2)

def euclideanY( row ):
	y1 = row['pickup_latitude']
	y2 = row['dropoff_latitude']
	return abs(y1-y2)



df[ 'distance' ] = df.apply(lambda row: euclidean(row), axis = 1)
df[ 'distanceX' ] = df.apply(lambda row: euclideanX(row), axis = 1)
df[ 'distanceY' ] = df.apply(lambda row: euclideanY(row), axis = 1)



print('distance', df['distance'].corr(df['fare_amount']))
print('distanceX', df['distanceX'].corr(df['fare_amount']))
print('distanceY', df['distanceY'].corr(df['fare_amount']))

df['distance_power05'] = df['distance'].pow(0.5)
print('distance_power05', df['distance_power05'].corr(df['fare_amount']))

# Istanbul taxi prices = initial + km x amount
#                        50 TL + 0 x 3
# Taxi price = time_value x time_amount + km_value x km_amount

# Taxi price = 30 x 0.01 + 20 x 0.02


# pickup_longitude	pickup_latitude	dropoff_longitude	dropoff_latitude
df['lon'] = df['pickup_longitude'] - df['dropoff_longitude']
df['lat'] = df['pickup_latitude'] - df['dropoff_latitude']

df['lon'] = df['lon'].abs()
df['lat'] = df['lat'].abs()

# df = df[ (df['lon'] < 0.001) & (df['lat'] < 0.001)]
print( df[[ 'fare_amount', 'pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']] )
print(df[[ 'fare_amount', 'pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']].describe())


# distance !
# real distance
# fuel consumption
# travel time --> traffic jam <-- fuel consumption
# 

"""
       pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude
count     293833.000000    293833.000000      293833.000000     293833.000000
mean         -73.975433        40.750736         -73.974376         40.751122
std            0.046888         0.035325           0.043571          0.038640
min          -79.535057        36.527530         -79.486418         35.561551
25%          -73.992333        40.736472         -73.991600         40.735378
50%          -73.982126        40.753308         -73.980620         40.753877
75%          -73.968467        40.767506         -73.965300         40.768402
max          -71.079100        42.338400         -71.089325         42.350588

"""

"""
for c in ['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']:
	df = df[ (df[c] > df[c].quantile(0.001)) & (df[c] < df[c].quantile(0.999)) ]
"""


print( df[['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']].describe() )


# Skip the scatter for now, (original)
#plt.scatter( df['pickup_longitude'], df['pickup_latitude'] )
#plt.scatter( df['dropoff_longitude'], df['dropoff_latitude'] )
#plt.show()


for c in ['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']:
	print(df[c].max() - df[c].min())

# 8.455956999999998     0.1  [ 85 ]
# 6.789037              0.1  [ 68 ]

xs = []
ys = []
for c in ['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']:
	df[ c ] = (df[c] - df[c].min()) / 0.01
	df[ c ] = df[c].astype(int)

plt.scatter( df['pickup_longitude'], df['pickup_latitude'] )

plt.show()


pickup_traffic = df.groupby( by = ['pickup_longitude','pickup_latitude']  ).size().to_dict()
dropoff_traffic = df.groupby( by = ['dropoff_longitude','dropoff_latitude']  ).size().to_dict()
df['pickup_traffic'] = df.apply( lambda row: pickup_traffic[ (int(row['pickup_longitude']), int(row['pickup_latitude'])) ] , axis = 1 )
df['dropoff_traffic'] = df.apply( lambda row: dropoff_traffic[ (int(row['dropoff_longitude']), int(row['dropoff_latitude'])) ] , axis = 1 )
print('pickup_traffic', df['fare_amount'].corr( df['pickup_traffic'] ))
print('dropoff_traffic', df['fare_amount'].corr( df['dropoff_traffic'] ))




pickup_traffic_time = df.groupby( by = ['pickup_longitude','pickup_latitude', 'time']  ).size().to_dict()
dropoff_traffic_time = df.groupby( by = ['dropoff_longitude','dropoff_latitude', 'time']  ).size().to_dict()
df['pickup_traffic_at_time'] = df.apply( lambda row: pickup_traffic_time[ (int(row['pickup_longitude']), int(row['pickup_latitude']), row['time']) ] , axis = 1 )
df['dropoff_traffic_at_time'] = df.apply( lambda row: dropoff_traffic_time[ (int(row['dropoff_longitude']), int(row['dropoff_latitude']), row['time']) ] , axis = 1 )
print('pickup_traffic_at_time', df['fare_amount'].corr( df['pickup_traffic_at_time'] ))
print('dropoff_traffic_at_time', df['fare_amount'].corr( df['dropoff_traffic_at_time'] ))



pickup_traffic_season = df.groupby( by = ['pickup_longitude','pickup_latitude', 'season']  ).size().to_dict()
dropoff_traffic_season = df.groupby( by = ['dropoff_longitude','dropoff_latitude', 'season']  ).size().to_dict()
df['pickup_traffic_at_season'] = df.apply( lambda row: pickup_traffic_season[ (int(row['pickup_longitude']), int(row['pickup_latitude']), row['season']) ] , axis = 1 )
df['dropoff_traffic_at_season'] = df.apply( lambda row: dropoff_traffic_season[ (int(row['dropoff_longitude']), int(row['dropoff_latitude']), row['season']) ] , axis = 1 )
print('pickup_traffic_at_season', df['fare_amount'].corr( df['pickup_traffic_at_season'] ))
print('dropoff_traffic_at_season', df['fare_amount'].corr( df['dropoff_traffic_at_season'] ))


print(df.shape)



no_travel = df[ df['distance'] < 0.00001 ]

time_value = no_travel.groupby(by = ['pickup_longitude','pickup_latitude'])['fare_amount'].mean().to_dict()
print( time_value )

def timelookup( row ):

	if (int(row['pickup_longitude']), int(row['pickup_latitude'])) in time_value:
		return time_value[ (int(row['pickup_longitude']), int(row['pickup_latitude'])) ]
	else:
		return 0

df['time_value'] = df.apply( lambda row: timelookup(row) , axis = 1 )

print("time_value", df['time_value'].corr( df['fare_amount'] ))


def path_area( row ):
	s = 0
	for x in range(row['pickup_longitude'], row['dropoff_longitude']):
		for y in range(row['pickup_latitude'], row['dropoff_latitude']):
			if (x,y) in pickup_traffic:
				s += pickup_traffic[ (x,y) ]
			if (x,y) in dropoff_traffic:
				s += dropoff_traffic[ (x,y) ]
	return s


df['path_area'] = df.apply(lambda row: path_area( row ), axis = 1)
print('path_area', df['path_area'].corr( df['fare_amount'] ))


df.to_csv("week7a_out.csv")


# sparse = mostly zero!
# has_second_car  (most of the people have only one or zero car)
# only very few of them has second car.
# mostly_zero


# azercell

# has x product [sparse]--> roaming
# has y product [sparse]--> telesecretary
# has z product [sparse]--> fax

# customerno    x y z TOTAL
# 83428429813   0 0 1 1
# ...........   0 1 0 1
# ...

# trying to make sparsity low!

# x,y,z are sparse

#! distance based - divide by fare, find the ratio

