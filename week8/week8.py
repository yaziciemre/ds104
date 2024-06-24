
import numpy as np
import pandas as pd
f = "week8_patient_dataset.csv"
Target = "hospital_death"

df = pd.read_csv(f)

# - descriptive analysis
# - removing outliers
# - removing unnecessary columns
# - filling nulls
# - feature mining, feature extraction, data enrichment

# - modelling


df = df.dropna()
df = df.select_dtypes(exclude = ['object'])
del df['hospital_id']
print(df)

"""
for i in range(len(df)):
	row = df.iloc[i].to_dict()
	s = []
	for r in row:
		s.append( r + '=' + str(row[r]) )

	s = " and ".join(s)
	print("if " + s)
"""



from sklearn.ensemble import RandomForestClassifier # Algorithm


success = []

for i in range(5):


	#: Shuffle, MUST
	df = df.sample(frac = 1.00) # %100


	# DONOT USE SAMPLE LIKE THESE BELOW
	train = df.sample(frac = 0.65)
	test  = df.sample(frac = 0.35)


	#: 80 (Train) - 20 (test) NOT A GOOD APPROACH
	#: 65 (Train) - 35 (test)

	# 99 train, 1 test (not enough to be sure that the algorithm has learnt)
	# 1 train, 99 test (not enough to learn)

	#: Calculate the split point
	train_ratio = 0.65
	train_count = int(train_ratio * len(df))

	#: Split into train and test (HORIZANTAL)
	train = df[ 0: train_count ] # from begining to train_count
	test  = df[ train_count:   ] # from train_count to end

	print(train.shape)
	print(test.shape)

	#: Split into X and Y (inputs and output!)
	train_y = train[ Target ]
	train_x = train.drop(columns = [Target])

	test_y = test[ Target ]
	test_x = test.drop(columns = [Target])


	clf = RandomForestClassifier(max_depth=5)
	clf.fit(train_x, train_y) # fit = train = learn = egitmek = ogrenmek = teach

	#: Create tahmins from test input!!!
	TAHMIN = clf.predict( test_x ) # infer, calculate, tahmin, execute formula 

	#: Test, how correct they are?
	result = (TAHMIN == test_y).astype(int)

	success.append( result.mean() )
	print(result.mean())

	# y = f( x )



print(success)
print(np.mean(success))
