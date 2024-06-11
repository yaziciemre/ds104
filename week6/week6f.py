
#: Imports
from ydata_profiling import ProfileReport
import warnings
import pandas as pd
import sys
import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#: Settings
warnings.filterwarnings("ignore")

#: Startup
filename = "w6_Loan_Default.csv"
df = pd.read_csv(filename)

#: Initial analysis
# profile = ProfileReport(df, title="Profiling Report")
# profile.to_file("week6_report.html")

#: If there is only one value in a column, delete it
#: Also, if the values of a column is %99.9 same, delete it
for c in df.columns:
	if df[c].nunique() == 1:
		print(bcolors.FAIL + 'Deleting column', c, 'because of single value', bcolors.ENDC)
		del df[c]

#: If most of the values in a column is null, delete it
for c in df.columns:
	if df[c].isnull().sum() / len(df) > 0.98:
		print(bcolors.FAIL + 'Deleting column', c, 'because of high ratio of nulls', bcolors.ENDC)
		del df[c]

#: Find me the columns where the mode has %99 percent of all data
for c in df.columns:
	mode_ratio = len(df[ df[c] == df[c].mode()[0] ]) / len(df)

	if mode_ratio > 0.99:
		print(bcolors.FAIL + 'Deleting column', c, 'because of imbalanced value', bcolors.ENDC)
		del df[c]

#: Find me the binary columns
for c in df.select_dtypes(include = ['object']):
	if df[c].nunique() == 2:
		#: Transform into a list
		lst = list(df[c].unique())
		if len(lst) == 2:
			#: Create a map
			replace = { lst[0]: 0, lst[1]: 1 }
			#: Replace the values
			df[c] = df[c].map( replace )
		else:
			lst = [i for i in lst if not pd.isna(i)]
			#: Create a map
			replace = { lst[0]: 0, lst[1]: 1, np.nan: np.nan }
			#: Replace the values
			df[c] = df[c].map( replace )


def remove_highly_correlated_columns(df, threshold=0.9):
    # Calculate the correlation matrix
    corr_matrix = df.select_dtypes(exclude = ['object']).corr().abs()
    
    # Select the upper triangle of the correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    
    # Find the columns with correlation greater than the threshold
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
    print(to_drop)
    # Drop the columns
    df.drop(columns=to_drop, inplace=True)
    
    return df

#: If there are two columns which have highly correlated, delete one of them
df = remove_highly_correlated_columns( df )

#: If there is too much columns, BAD, complexity
#: If there is few columns,      BAD, could not predict
#: To do that, first we eliminate as much as possible (! not useful ones)

#: Remove the items which has extremely outliers
df = df[ df['income'] < 15720 ]
df = df[ df['LTV'] < 100 ]

#: How to use categorical variables

# APPROACH 1: Transform into Dummy
# NOTE, only use it for less amount of values (not like city)
df = pd.get_dummies( df, columns = ['loan_purpose', 'Gender', 'loan_type', 'Region'] )

# APPROACH 2: Most/Mode and others if it is highly imbalanced
# NOTE: A little data loss
df['total_units'] = df['total_units'].map({'1U': 0, '2U': 1, '3U': 1, '4U': 1})

# APPROACH 3: Ordinal variables can be replaced with values
# NOTE: A little data loss
age_map = {'<25': 20, '25-34': 30, '35-44': 40, '45-54': 50, '55-64': 60, '65-74': 70, '>74': 80}
df['age'] = df['age'].map(age_map)

# APPROACH 4: Replace with frequencies
# Motto: if something is used most, is important, if there are too many values
# NOTE: A little data loss
freq_map = df['occupancy_type'].value_counts().to_dict()
df['occupancy_type'] = df['occupancy_type'].map( freq_map )

# APPROACH 5: Target average (best approach)
# NOTE: A little data loss
TARGET = 'Status'
avg_map = df.groupby( by = ['credit_type'])[TARGET].mean().to_dict()
df['credit_type'] = df['credit_type'].map( avg_map )

# =================
# Later on

#: Delete the columns which have very low correlation to "TARGET"
for c in df.columns:
	corr = abs(df[c].corr(df[TARGET]))
	if corr < 0.02:
		print(bcolors.FAIL + 'Deleting column', c, 'because of low correlation', bcolors.ENDC)
		del df[c]

#: Transform true/false into 1/0
for c in df.select_dtypes(include = ['bool']):
	df[c] = df[c].astype(int)

#: Scaling
df = df[ df['loan_amount'] > 100000 ]
df = df[ df['loan_amount'] < 2000000 ]
# df['loan_amount'] = df['loan_amount'] / 1000
df['loan_amount'] = df['loan_amount'] - df['loan_amount'].min()
df['loan_amount'] = df['loan_amount'] / df['loan_amount'].max()




items_to_scale = ['property_value', 'income']
for i in items_to_scale:
	df[ i ] = df[ i ] - df[ i ].min()
	df[ i ] = df[ i ] / df[ i ].max()



df.to_csv("week6f.csv")



