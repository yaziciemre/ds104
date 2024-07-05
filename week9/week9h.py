import re
import pandas as pd
import warnings

warnings.filterwarnings("ignore")
s = "week9_input_bcell.csv"
df = pd.read_csv(s)

#for x in df.groupby(by = ['parent_protein_id']):
#	print(x[1]['target'].mean())

def repeating( value ):
	if re.match(r".*([A-Z])\1.*", value):
		return 1
	else:
		return 0

df['peptide_seq_REP'] = df['peptide_seq'].apply( repeating )
print(df['peptide_seq_REP'].corr(df['target']))


df['p_F'] = df['peptide_seq'].apply(lambda value: value[0])
df['p_L'] = df['peptide_seq'].str.len()

print(df.groupby(by = ['p_F'])['target'].mean())
print(df.groupby(by = ['p_L'])['target'].mean())
"""
for a in "ABCDEFGHIJKLMNOPRSTUVYZWXQ":
	for b in "ABCDEFGHIJKLMNOPRSTUVYZWXQ":
		
		df[a+b] = df['protein_seq'].apply(lambda value: value.count(a+b))
		c = df[a+b].corr(df['target'])
		if abs(c) > 0.10:
			print(a+b, c)
"""
# print(df['start_position'].corr(df['target']))
# print(df['end_position'].corr(df['target']))
# print( df['parent_protein_id'].nunique() )


print(df.select_dtypes(exclude = ['object']).corr()['target'])

df['protein_seq_L'] = df['protein_seq'].str.len()
print(df['protein_seq_L'].corr(df['target']))


