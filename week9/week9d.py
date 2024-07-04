import re
s = "week9_booking.csv"
import pandas as pd
df = pd.read_csv(s)

target = 'booking status'

del df['Booking_ID']
df['booking status'] = df['booking status'].map(
	{'Not_Canceled': 0, 'Canceled': 1}
)

def formatter( i: str ) -> str:
	return re.sub("[0-9]", "#", i)

df['date of reservation_FMT'] = df['date of reservation'].apply(formatter)
formats = df['date of reservation_FMT'].value_counts().to_dict()

t = '####-#-##'
df = df[ df['date of reservation_FMT'] != t ]
del df['date of reservation_FMT']

df['date of reservation'] = pd.to_datetime( df['date of reservation'] )


#: Categoric variables
for c in ['type of meal', 'room type', 'market segment type']:
	print(df[c].value_counts())

#: 
df['type of meal_1'] = df['type of meal'].map( 
	{'Meal Plan 1': 1, 'Not Selected': 0, 'Meal Plan 2': 0, 'Meal Plan 3': 0} 
)

df['type of meal_2'] = df['type of meal'].map( 
	{'Meal Plan 1': 1, 'Not Selected': 1, 'Meal Plan 2': 0, 'Meal Plan 3': 0} 
)

df['type of meal_3'] = df['type of meal'].map( 
	{'Meal Plan 1': 1, 'Not Selected': 0, 'Meal Plan 2': 1, 'Meal Plan 3': 1} 
)

print(df['type of meal_1'].corr(df[target]))
print(df['type of meal_2'].corr(df[target]))
print(df['type of meal_3'].corr(df[target]))

top2 = list( df['room type'].value_counts().to_dict().keys() )[0:2]
mapper = {}
for c in df['room type'].unique():
	if c in top2:
		mapper[ c ] = c
	else:
		mapper[ c ] = 'others'

print(mapper)
df['room type'] = df['room type'].map( mapper )

print(df['room type'])


for c in df['market segment type'].unique():
	print(c, df[df['market segment type'] == c][target].mean())


import matplotlib.pyplot as plt
xs = []
ys = []
for c in df['lead time'].unique():
	xs.append(c)
	ys.append( df[ df['lead time'] == c ][target].mean() )


print(  df['lead time'].corr( df[target] ) )

plt.scatter( xs, ys )
plt.show()