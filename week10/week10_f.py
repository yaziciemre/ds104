import matplotlib.pyplot as plt
import pandas as pd

# Assignment:
# Find a way to assign the values of threshold 1, and 2
# Do not use 6 parameters!
# Use somehow a default value!

# method: commonInDataset
# Finds the common values in a given dataset, column by column
# @df, pd.DataFrame: The input dataframe
# @categoric_threshold: The threshold for categorical variables
# @binary_threshold: The threshold for binary variables
# @numeric_threshold: The threshold for numeric variables
# @return, list: A list of common properties (as dictionaries)
# @completed
def commonInDataset( df: pd.DataFrame, categoric_threshold: float = 0.40, binary_threshold: float = 0.70, numeric_threshold: float = 0.30 ) -> list:
	#: Declare variables
	results = []

	#: For object type / categorical variables
	for c in df.select_dtypes(include = ['object']):
		most = list(df[c].value_counts(normalize = True).to_dict().items())[0]
		if most[1] > categoric_threshold:
			how_sharp = 'normal'
			if most[1] > 0.80:
				how_sharp = 'very_sharp'
			elif most[1] > 0.60:
				how_sharp = 'sharp'
			results.append( {'column': c, 'type': 'categoric', 'common': most[0], 'sharpness': how_sharp} )

	#: For binary and numeric
	for c in df.select_dtypes(exclude = ['object']):
		#: If binary?
		if df[c].nunique() == 2:
			most = list(df[c].value_counts(normalize = True).to_dict().items())[0]
			how_sharp = 'normal'
			if most[1] > binary_threshold:
				if most[1] > 0.90:
					how_sharp = 'very_sharp'
				elif most[1] > 0.80:
					how_sharp = 'sharp'
				results.append( {'column': c, 'type': 'binary', 'common': most[0], 'sharpness': how_sharp} )
		else:
			#: Find mean, std and zscore
			m = df[c].mean()
			s = df[c].std()
			r = s / m

			if r < numeric_threshold:

				how_sharp = 'normal'
				if r < 0.10:
					how_sharp = 'very_sharp'
				elif r < 0.20:
					how_sharp = 'sharp'

				results.append( {'column': c, 'type': 'numeric', 'common': m, 'sharpness': how_sharp} )
	
	#: Return
	return results




def differentInDatasets( df1: pd.DataFrame, df2: pd.DataFrame ) -> list:
	#: Find the commons in df1, df2
	c1 = commonInDataset( df1 )
	c2 = commonInDataset( df2 )
	#: First, if there is an exact line in df1 and df2, remove!<
	d1 = [ i for i in c1 if i not in c2 ]
	d2 = [ i for i in c2 if i not in c1 ]


	# complete the code here!!!
#a {'column':'year',  'common': 27.390214303692783, 'sharpness': 'sharp'}
#b {'column':'year', 'common': 30.57358457416436, 'sharpness': 'very_sharp'}
#a {'column':'condition',  'common': 3.252971931248155, 'sharpness': 'normal'}
#b {'column':'condition', 'common': 4.081724000883197, 'sharpness': 'sharp'}

 

	pass


s = "week6_car_prices.csv"
t = 'sellingprice'
df = pd.read_csv(s, on_bad_lines='skip')
df['year'] = df['year'] - df['year'].min()

a = df[ df[t] < 20000 ]
b = df[ df[t] >= 20000 ]

results = commonInDataset( a )
for r in results:
	print('a', r)

results = commonInDataset( b )
for r in results:
	print('b', r)


x = differentInDatasets( a, b )

"""

a {'column': 'body', 'type': 'categoric', 'common': 'Sedan', 'sharpness': 'normal'}
a {'column': 'transmission', 'type': 'categoric', 'common': 'automatic', 'sharpness': 'very_sharp'}
a {'column': 'interior', 'type': 'categoric', 'common': 'black', 'sharpness': 'normal'}
a {'column': 'year', 'type': 'numeric', 'common': 27.390214303692783, 'sharpness': 'sharp'}
a {'column': 'condition', 'type': 'numeric', 'common': 3.252971931248155, 'sharpness': 'normal'}

b {'column': 'transmission', 'type': 'categoric', 'common': 'automatic', 'sharpness': 'very_sharp'}
b {'column': 'interior', 'type': 'categoric', 'common': 'black', 'sharpness': 'normal'}
b {'column': 'year', 'type': 'numeric', 'common': 30.57358457416436, 'sharpness': 'very_sharp'}
b {'column': 'condition', 'type': 'numeric', 'common': 4.081724000883197, 'sharpness': 'sharp'}
"""

