import re
import pandas as pd
import sys
s = "week9_news.csv"
df = pd.read_csv(s)
df = df.dropna()
del df['Unnamed: 0']
df['label'] = df['label'].map({'REAL': 1, 'FAKE': 0})
print(df)

def cleanup( text: str ) -> str:
	return re.sub("[^A-Za-z0-9 ]", "", text)


df['lentitle'] = df['title'].str.len()
# df['wctitle'] = df['title'].apply( lambda value: len(value.split(' ')) + 1 )
df['punctitle'] = df['title'].apply( lambda value: len(value) - len(re.sub("[^A-Za-z0-9 ]", "" , value))  )
#df['digittitle'] = df['title'].apply( lambda value: len(value) - len(re.sub("[^0-9]", "" , value))  )
#df['capitaltitle'] = df['title'].apply( lambda value: len(value) - len(re.sub("[^A-Z]", "" , value))  )
df['startitle'] = df['title'].apply( lambda value: any(x in value for x in ['*', '#', '@']) )
df['startitle'] = df['startitle'].astype(int)
df['uppertitle3'] = df['title'].apply( 
	lambda value: 
	1 if re.match( r'[A-Z]{3,}', str(value) ) else 0 
)


df['text_cleaned'] = df['text'].apply(cleanup)
df['lentext'] = df['text_cleaned'].str.len()
df['ratio'] = df['title'].str.len() / df['text'].str.len()
print(df['ratio'].corr(df['label']))



df['uppertitle4'] = df['title'].apply( 
	lambda value: 
	1 if re.match( r'[A-Z]{4,}', str(value) ) else 0 
)

"""
if re.match('', ''):
	return 1
else:
	return 0
"""


fakes = df[ df['label'] == 0 ]
reals = df[ df['label'] == 1 ]

del fakes['label']
del reals['label']

print(fakes.describe())
print(reals.describe())

fakes = fakes.sample(frac = 1.0)
reals = reals.sample(frac = 1.0)

print(list(fakes['title'].head(10)))
print(list(reals['title'].head(10)))

print(len(fakes))
print(len(reals))

rs = {}
fs = {}



for i in range(len(reals)):
	title = cleanup(reals.iloc[i]['title'])
	for word in title.lower().split(' '):
		if word in rs:
			rs[word] += 1
		else:
			rs[word] = 1


for i in range(len(fakes)):
	title = cleanup(fakes.iloc[i]['title'])
	for word in title.lower().split(' '):
		if word in fs:
			fs[word] += 1
		else:
			fs[word] = 1


allwords = list(rs.keys()) + list(fs.keys())
#: Make unique
allwords = list(set(allwords))


df['title_cleaned'] = df['title'].apply(cleanup)
df['title_cleaned'] = df['title_cleaned'].str.lower()


import random

"""
for _ in range(1000):


	limit1 = random.randint(1, 10)
	limit2 = random.randint(limit1, 20)
	limit3 = random.randint(limit2, 30)

	f_e = [] # fake extreme
	f_h = [] # fake high
	f_m = [] # fake medium

	r_e = [] # real extreme
	r_h = [] # real high
	r_m = [] # real medium

	for w in allwords:
		r = 0 # real freqeuncy
		f = 0 # fake freqeuncy

		if w in fs:
			f = fs[w]

		if w in rs:
			r = rs[w]

		if f>r:
			if f-r > limit3:
				f_e.append( w )
			elif f-r > limit2:
				f_h.append( w )
			elif f-r > limit1:
				f_m.append( w )

		if r>f:
			if r-f > limit3:
				r_e.append( w )
			elif r-f > limit2:
				r_h.append( w )
			elif r-f > limit1:
				r_m.append( w )


	df['r_e'] = df['title_cleaned'].apply( lambda value: sum([1 if w in r_e else 0 for w in value.split(' ')]) )
	df['r_h'] = df['title_cleaned'].apply( lambda value: sum([1 if w in r_h else 0 for w in value.split(' ')]) )
	df['r_m'] = df['title_cleaned'].apply( lambda value: sum([1 if w in r_m else 0 for w in value.split(' ')]) )

	df['f_e'] = df['title_cleaned'].apply( lambda value: sum([1 if w in f_e else 0 for w in value.split(' ')]) )
	df['f_h'] = df['title_cleaned'].apply( lambda value: sum([1 if w in f_h else 0 for w in value.split(' ')]) )
	df['f_m'] = df['title_cleaned'].apply( lambda value: sum([1 if w in f_m else 0 for w in value.split(' ')]) )

	total_correl = 0
	max_correl = 0
	for c in ['r_e','r_h','r_m','f_e','f_h','f_m']:
		total_correl += abs(df[c].corr(df['label']))
		cc = abs(df[c].corr(df['label']))
		if cc > max_correl:
			max_correl = cc
		
	if total_correl > 2.0 and max_correl > 0.5:
		print(f"{limit1}\t{limit2}\t{limit3}\t{total_correl}\t{max_correl}")
"""




limit1 = 1
limit2 = 13
limit3 = 27

f_e = [] # fake extreme
f_h = [] # fake high
f_m = [] # fake medium

r_e = [] # real extreme
r_h = [] # real high
r_m = [] # real medium

for w in allwords:
	r = 0 # real freqeuncy
	f = 0 # fake freqeuncy

	if w in fs:
		f = fs[w]

	if w in rs:
		r = rs[w]

	if f>r:
		if f-r > limit3:
			f_e.append( w )
		elif f-r > limit2:
			f_h.append( w )
		elif f-r > limit1:
			f_m.append( w )

	if r>f:
		if r-f > limit3:
			r_e.append( w )
		elif r-f > limit2:
			r_h.append( w )
		elif r-f > limit1:
			r_m.append( w )


df['r_e'] = df['title_cleaned'].apply( lambda value: sum([1 if w in r_e else 0 for w in value.split(' ')]) )
df['r_h'] = df['title_cleaned'].apply( lambda value: sum([1 if w in r_h else 0 for w in value.split(' ')]) )
df['r_m'] = df['title_cleaned'].apply( lambda value: sum([1 if w in r_m else 0 for w in value.split(' ')]) )

df['f_e'] = df['title_cleaned'].apply( lambda value: sum([1 if w in f_e else 0 for w in value.split(' ')]) )
df['f_h'] = df['title_cleaned'].apply( lambda value: sum([1 if w in f_h else 0 for w in value.split(' ')]) )
df['f_m'] = df['title_cleaned'].apply( lambda value: sum([1 if w in f_m else 0 for w in value.split(' ')]) )


dx = df.drop( columns = ['title', 'title_cleaned', 'text', 'text_cleaned'] )

y = dx['label']
X = dx.drop(columns = ['label'])

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)
print(clf.score(X,y))
print(X.columns)
print(list(clf.feature_importances_))


X.corr().to_csv("week9e_corr.csv")







