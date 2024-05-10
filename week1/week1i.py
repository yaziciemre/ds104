
#: Import libraries
import json

#! open command opens a file

#: Open and load the data
data1 = json.load(open('week1i.json', 'r'))
data2 = json.load(open('week1i-2.json', 'r'))



print(data1)






counts = {}

for item in data1:
	
	if item['major'] not in counts:
		counts[ item['major'] ] = 1
	else:
		counts[ item['major'] ] = counts[ item['major'] ] + 1


print(counts)
print(max(counts, key=counts.get))