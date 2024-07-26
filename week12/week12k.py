
"""
import random
s = "week11_customer_data.csv"
import pandas as pd
df = pd.read_csv(s)

id_map = {
	#'correct': 'shuffled'
}
ids = list(df['id'].values)
random.shuffle(ids)
id_map = dict(zip(ids, [i for i in range(len(ids))]))
df['id'] = df['id'].map(id_map)
print(df)
del ids
"""
from sklearn.ensemble import RandomForestClassifier
import os
import pickle
import pandas as pd
df = pd.read_csv("week9_stroke_data.csv")
df = df.dropna()
y = df['stroke']
x = df.drop(columns = ['stroke'])

# preprocessing, limiting, feature mining ..... [12 steps]

clf = None

# If the file week12_model.pkl exists!
if os.path.isfile('week12_model.pkl'):
	print('Model has already been saved, so it is going to be loaded')
	#: Resume
	file = open('week12_model.pkl', 'rb') # Open a file for [R]EADING, [B]INARY
	clf = pickle.load(file)
	file.close()
else:
	print('Model has not been saved yet, so we train')
	clf = RandomForestClassifier(max_depth=4, random_state=0)
	clf.fit(x, y)
	#: Save to file
	# Like saving "computer game" to a file, so that we can continue from that point
	# open a file, where you ant to store the data
	file = open('week12_model.pkl', 'wb') # open a file for [W]RITING not for READING, and [B]INARY not TEXTUAL
	pickle.dump(clf, file)
	file.close()


print(clf)
