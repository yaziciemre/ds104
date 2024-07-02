
import pandas as pd
s = "week9_Loan_default.csv"
df = pd.read_csv(s)
TARGET = 'Default'
#: Remove the unique column
del df['LoanID']

#: Replace YES/NO
df = df.replace('Yes', 1)
df = df.replace('No', 0)

#: Create a new
df['DTTRatio'] = df['LoanAmount'] / df['Income']
df['SumofHas'] = df['HasMortgage'] + df['HasDependents'] + df['HasCoSigner']
df['GoodPayerEducation'] = df[ 'Education' ].isin( ["Master's", "PhD"] )


ratios = {}
cat = ['Education', 'EmploymentType', 'MaritalStatus', 'LoanPurpose']
for c in cat:
	ratios[c] = {}
	print(c)
	for v in df[c].unique():
		print('    ', v, len(df[ df[c] == v ]), round(df[ df[c] == v ][TARGET].mean(), 3))
		ratios[c][v] = round(df[ df[c] == v ][TARGET].mean(), 3)

	print('--------------------------')

print(ratios)

{
	'Education': {"Bachelor's": 0.121, "Master's": 0.109, 'High School': 0.129, 'PhD': 0.106}, 
	'EmploymentType': {'Full-time': 0.095, 'Unemployed': 0.136, 'Self-employed': 0.115, 'Part-time': 0.12}, 
	'MaritalStatus': {'Divorced': 0.125, 'Married': 0.104, 'Single': 0.119}, 
	'LoanPurpose': {'Other': 0.118, 'Auto': 0.119, 'Business': 0.123, 'Home': 0.102, 'Education': 0.118}
}

for c in cat:
	df[c] = df[c].map( ratios[c] )
	print(df[c].corr(df[TARGET]))



# 1- Dummy
# 2- Target average
# 3- Most
# 4- Usage Ratio
# 5- Most 3
