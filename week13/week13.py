


import pandas as pd

df = pd.read_csv("")

freq = {}

for c in df['news'].values:
	words = c.split(" ")
	for word in words:
		if word in freq:
			freq[word] += 1
		else:
			freq[word] = 1

print(freq['tree'])

