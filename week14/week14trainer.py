
import pandas as pd

df = pd.read_csv("week14_processed.csv")

#: Shuffle
df = df.sample(frac = 1.0)
target = 'price'

average = df[target].mean()
df[target] = df[target] - average

train_size = int(len(df) * 0.70)

train = df[:train_size]
test = df[train_size:]


train_y = train[ target ]
train_x = train.drop(columns = [target])

test_y = test[ target ]
test_x = test.drop(columns = [target])


from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

for _ in range(10):
	regr = RandomForestRegressor(max_depth=6)
	regr.fit(train_x, train_y)
	print( regr.score(test_x, test_y) )

