
import sys
import pandas as pd
s = "week9_smoke_train_dataset.csv"
df = pd.read_csv(s)

target = 'smoking'

df = df.select_dtypes(exclude = ['object'])

df = df.sample(frac = 1.0)
half = int(len(df) / 2)
train = df[:half]
test = df[half:]


train_y = train[target]
train_X = train.drop(columns = [target])

test_y = test[target]
test_X = test.drop(columns = [target])


from sklearn.ensemble import RandomForestClassifier
for n in [10, 50, 100, 150, 200]:
	for c in [2,3,4,5,6,7,8,9]:
		clf = RandomForestClassifier(max_depth=c, random_state=0, n_estimators = n)
		clf.fit(train_X, train_y)
		print(c, n, clf.score(test_X, test_y))



sys.exit(1)
df['predicted'] = clf.predict(X)
df['real'] = y

df['correct'] = df['predicted'] = df['real']

df.to_csv('week9i.csv')

no = df[ df['correct'] == True ].mean().to_dict()
yes = df[ df['correct'] == False ].mean().to_dict()
for i in yes:
	print(i, yes[i], no[i])


