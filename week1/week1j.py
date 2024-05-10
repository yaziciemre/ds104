import json
import random
#: Open and load the data
data1 = json.load(open('week1i.json', 'r'))

print(data1)



d = {'x': 'y', 'z': 'p', 't': 3}



d['t'] = 4 # updates the value if there is already key in the dictionary
d['q'] = 18  # adds a new item automatically, because there is no such item




# {'name': 'Victor Lee', 'age': 23, 'major': 'Marketing', 'gender': 'Male'}
"""
 {'name': 'Victor Lee', 'age': 23, 'major': 'Marketing', 'gender': 'Male', 'grades': 
	{
		'math': 67,
		'physiscs': 90,
		'business admin': 60
	}

 }
""" 
# multi line comment


# {'name': 'Victor Lee', 'age': 23, 'major': 'Marketing', 'gender': 'Male', 'grades': 
#	{
#		'math': 67,
#		'physiscs': 90,
#		'business admin': 60
#	}
#
# }






for d in data1:
	d['grades'] = {
		'math': int(random.random() * 100),
		'science': int(random.random() * 100)
	}

	print(d)

















