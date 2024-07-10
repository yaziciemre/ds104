import sys
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import warnings
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings('ignore')
s = "week9_Loan_default.csv"
df = pd.read_csv(s)
t = "Default"

"""
# highly imbalanced
# ===============
ones = df[ df[t] == 1 ]
# zeros = df[ df[t] == 0 ].sample(frac = 0.3)
zeros = df[ df[t] == 0 ].sample(n = len(ones))
df = pd.concat( [ones, zeros] )
# a little bit more balanced
# ===============
"""

df = df.replace('Yes', 1)
df = df.replace('No', 0)
df = pd.get_dummies( df , columns = ['Education','EmploymentType','MaritalStatus','LoanPurpose'])
del df['LoanID']

#: Drop none
df = df.dropna()

#: Sample, shuffle
df = df.sample(frac = 1.0) # 88 - 12

#: Split
loc = int(len(df) * 0.70)
train = df[ :loc ] # 88 - 12

ones  = train[ train[t] == 1 ]
zeros = train[ train[t] == 0 ].sample(frac = 0.14) # n = len(ones)

print("train ones ", len(ones))
print("train zeros", len(zeros))

train = pd.concat( [ones, zeros] )
train = train.sample(frac = 1.0)

test =  df[ loc: ] # 88 - 12

train_y = train[t]
train_x = train.drop(columns = [t])

test_y = test[t]
test_x = test.drop(columns = [t])

clf = RandomForestClassifier(max_depth=5, random_state=0)
clf.fit(train_x, train_y)

print(clf.score(test_x, test_y))

"""
age ==> 

std
mean
quartile
median
mode
....
"""

test[ 'pred' ] = clf.predict( test_x )
test[ 'prob' ] = clf.predict_proba(test_x)[:,1]
# test[ 'real' ] = test_y



for T in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:

	test['pred'] = test['prob'] > T

	test['correct'] = (test[t] == test['pred'])

	test['TP'] = ((test['correct'] == True) & (test['pred'] == 1)).astype(int)
	test['TN'] = ((test['correct'] == True) & (test['pred'] == 0)).astype(int)
	test['FP'] = ((test['correct'] == False) & (test['pred'] == 1)).astype(int)
	test['FN'] = ((test['correct'] == False) & (test['pred'] == 0)).astype(int)

	test['correct'] = test['correct'].astype(int)


	print("correct.avg",  test['correct'].mean())
	print("target .avg",  test[t].mean())
	print("predict.avg",  test['pred'].mean())

	trues = test[ test['correct'] == True ]
	falses = test[ test['correct'] == False ]

	print("trues  .avg", trues['pred'].mean())
	print("falses .avg", falses['pred'].mean())




	# the probability of being "TRUE/CORRECT" for the records which the 
	# algorithms says they are 1s or 0s
	print( "pred=1. avg", test[ test['pred'] == 1 ]['correct'].mean() )
	print( "pred=0. avg", test[ test['pred'] == 0 ]['correct'].mean() )

	print( "TP      avg", test['TP'].mean() )
	print( "TN      avg", test['TN'].mean() )
	print( "FP      avg", test['FP'].mean() )
	print( "FN      avg", test['FN'].mean() )


	print('threshold', T)
	print("accuracy   ", accuracy_score(test[t], test['pred']))
	print("f1score    ", f1_score(test[t], test['pred']))





test.to_csv("week10b_out.csv")





sys.exit(1)
import matplotlib.pyplot as plt
from sklearn import tree
fn=list(test_x.columns)
cn=['1', '0']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=1600)
tree.plot_tree(clf.estimators_[0],
               feature_names = fn, 
               class_names=cn,
               filled = True);
fig.savefig('week10_rf_individualtree.png')



import os
from sklearn.tree import export_graphviz

for i in range(100):
	print('plotting',i)
	export_graphviz(clf.estimators_[i],
	                feature_names=test_x.columns,
	                filled=True,
	                rounded=True, out_file = 'tree.dot', class_names = ['no', 'yes'])

	os.system(f'dot -Tpng tree.dot -o trees/week10_tree{i}.png')