
file = "week5c.csv"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(file)
print(df)

# 26| Save to excel
#df.to_excel("week5_output.xlsx", sheet_name='Sheet_name_1')  

# 27| to_json
print( df[['arrival_date_month','is_canceled']].head(10).to_json() )

# 28| to_html
print(df.head(100).to_html())

with open('week5d.html', 'w') as fo:
    fo.write(df.head(100).to_html())

# 29| Clipboard
#df.head(3).to_clipboard()

# 30| to_markdown()
print( df[['arrival_date_month','is_canceled']].head(10).to_markdown() )

print(df)

# 31| Data Grouping
for g in df.groupby(by = ['market_segment']):
	print(g[0])
	print(g[1])


for v in df['market_segment'].unique():
	sub_df = df[ df['market_segment'] == v ]
	print(">>", v)
	print("<<", sub_df)



print( df.groupby(by = ['country'])['children'].mean().to_dict() )
# SELECT country, AVG(children) FROM visitors GROUP BY country


a = ['ahmet', 'mehmet', 'zeyneb']
a = [i.title() for i in a]


children_ratio = df.groupby(by = ['country'])['children'].mean().to_dict()
children_ratio = {k:round(v, 3) for k,v in children_ratio.items()}
children_ratio = {k: v for k, v in sorted(children_ratio.items(), key=lambda item: item[1])}
children_ratio = list( children_ratio.items() )
print(children_ratio)
print(len(children_ratio))

# 1| SORT INDEX
# 2| VALUE INDEX
# 3| QUARTILE?


# --> 1|
group_len = int(len(children_ratio) / 5)
print(group_len)

group1 = children_ratio[0:34]
group2 = children_ratio[34:68]
group3 = children_ratio[68:102]
group4 = children_ratio[102:136]
group5 = children_ratio[136:]

print(group1)
print(group2)
print(group3)
print(group4)
print(group5)

# --> 2|

group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
for i in range(len(children_ratio)):
	# ('UKR', 0.118)
	value = children_ratio[i][1]
	if value < 0.04:
		group1.append( children_ratio[i] )
	elif value < 0.10:
		group2.append( children_ratio[i] )
	elif value < 0.20:
		group3.append( children_ratio[i] )
	elif value < 0.40:
		group4.append( children_ratio[i] )
	else:
		group5.append( children_ratio[i] )


print('==========================================')
print(group1)
print(group2)
print(group3)
print(group4)
print(group5)


import json


ratios = []

for i in children_ratio:
	ratios.append(i[1])


print('==========================================')
print('==========================================')
print('==========================================')
print('==========================================')
print(ratios)


# Discard the items before 95th
ratios = ratios[145:]

index = 10
ratios0 = ratios[:index]
ratios1 = ratios[index:]

print(np.mean(ratios0), np.std(ratios0))
print(np.mean(ratios1), np.std(ratios1))





