
from stemmer import PorterStemmer
import pandas as pd

df = pd.read_csv("data/7282_1.csv")
target = "reviews.rating"
s = PorterStemmer()


#: Remove the columns with no variation
for c in df:
	if df[c].nunique() < 2:
		print("deleting column", c)
		del df[c]

#: Remove where the target is null
df = df[ df[target].notnull() ]
#: Drop the duplicates
df = df.drop_duplicates()


del df['latitude']
del df['longitude']
del df['city']
del df['postalCode']
del df['province']
del df['address']
del df['reviews.username']


freqs = {}

def downcast( category: str ) -> str:
	global freqs
	category = category.lower()
	category = category.replace(" & ", ",")
	items = category.split(',')
	items = [s.stem(i) for i in items]
	items = list(set(items))
	items.sort()

	for w in items:
		if w not in freqs:
			freqs[w] = 1
		else:
			freqs[w] += 1

	r = ",".join(items)
	if r == 'hotel,hotels':
		r = 'hotels'
	return r

df['categories'] = df['categories'].apply(downcast)

for c in df['categories'].unique():
	print( df[df['categories']==c]['name'].nunique(), c)

print("number of categories", df['categories'].nunique())

#: Sort by values (frequencies, reverse order)
#: And get the first 7 items
freqs = sorted(freqs.items(), key=lambda x:x[1], reverse=True)[0:7]
#: Get only the names
freqs = [f[0] for f in freqs]

#: Create new features
for f in freqs:
	df[f] = df['categories'].apply(lambda value: f in value).astype(int)

#: Most
df['most'] = (df['categories'] == 'hotel').astype(int)
del df['categories']

del df['reviews.date']
del df['reviews.dateAdded']


print(df['reviews.username'].value_counts())


df.to_csv("week14a.csv")