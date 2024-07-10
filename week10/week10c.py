import numpy as np
import sys
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import warnings
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings('ignore')
s = "week8_patient_dataset.csv"
t = "hospital_death"
df = pd.read_csv(s)

del df['hospital_id']
df['gender'] = df['gender'].map({'M': 1, 'F': 0})
df = df.select_dtypes( exclude = ['object'] )
df = df.dropna()


# ================================================================

BF = 0.25 # balancing fraction
TTS = 0.65 # train test split
MD = 6 # max depth
TH = 0.5 # threshold


WEIGHTS = {
	'FP': 1,
	'FN': 0.1,
	'TN': 0.005,
	'TP': 0.5
}


for TH in [0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.9]:

	"""
	for F in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]:
		results = []
		for _ in range(5):
	"""		

	#: Sample, shuffle
	df = df.sample(frac = 1.0)

	#: Split
	loc = int(len(df) * TTS)
	train = df[ :loc ] 

	ones  = train[ train[t] == 1 ]
	zeros = train[ train[t] == 0 ].sample(frac = BF) 

	train = pd.concat( [ones, zeros] )
	train = train.sample(frac = 1.0)

	test =  df[ loc: ]

	train_y = train[t]
	train_x = train.drop(columns = [t])

	test_y = test[t]
	test_x = test.drop(columns = [t])

	clf = RandomForestClassifier(max_depth=MD, random_state=0)
	clf.fit(train_x, train_y)
	#print("MD", MD, "TTS", TTS, "BF", BF, f1_score( test_y, clf.predict(test_x) ))




	if 'correct' in test_x:
		test_x = test_x.drop(columns = ['correct', 'prob', 'pred', 'real', 'TN', 'TP', 'FN', 'FP'])

	test_x['prob'] = clf.predict_proba( test_x )[:,1]
	test_x['pred'] = (test_x['prob'] >= TH).astype(int)
	test_x['real'] = test_y

	test_x['correct'] = ( test_x['real'] == test_x['pred'] ).astype(int)

	test_x['TP'] = ((test_x['correct'] == True) & (test_x['pred'] == 1)).astype(int)
	test_x['TN'] = ((test_x['correct'] == True) & (test_x['pred'] == 0)).astype(int)
	test_x['FP'] = ((test_x['correct'] == False) & (test_x['pred'] == 1)).astype(int)
	test_x['FN'] = ((test_x['correct'] == False) & (test_x['pred'] == 0)).astype(int)

	weighted_accuracy = 0
	for w in WEIGHTS:
		weighted_accuracy += WEIGHTS[w] * test_x[w].mean()
	weighted_accuracy = weighted_accuracy / sum(WEIGHTS.values())

	# test_x[['correct', 'prob', 'pred', 'real', 'TN', 'TP', 'FN', 'FP' ] ].describe().round(3)

	print( TH,"F1", f1_score(test_x['real'], test_x['pred']), "WA", weighted_accuracy )

