import warnings
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings('ignore')
s = "week9_hypertension_data.csv"
df = pd.read_csv(s)
t = "target"

#: Drop none
df = df.dropna()

#: Sample, shuffle
df = df.sample(frac = 1.0)

#: Split
loc = int(len(df) * 0.60)
train = df[ :loc ]
test =  df[ loc: ]

train_y = train[t]
train_x = train.drop(columns = [t])

test_y = test[t]
test_x = test.drop(columns = [t])

clf = RandomForestClassifier(max_depth=4, random_state=0)
clf.fit(train_x, train_y)

print(clf.score(test_x, test_y))

test[ 'pred' ] = clf.predict( test_x )
# test[ 'real' ] = test_y



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

test.to_csv("week10_out.csv")


# ==============================================================
# Error/Prediction Modeling Rules:
# ==============================================================

# 1- Target average should not be different than predicted average
#    there are many ways to overcome this problem
#    e.g. voting or using multiple predictors is a method
# 
# 2- Analyse Common of trues and falses
#    