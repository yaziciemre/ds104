
# pip == python installation pipeline
# This is a tool to install a library / package

# pip -V
# pip 23.3.2 from site-packages/pip (python 3.9)

# to Install a library, use 
# pip install numpy


import matplotlib.pyplot as plt

# Numerical operations
# import numpy
# numpy.mean(...)

import numpy as np
# np.mean(...)



# Python Import, Baska bir kutuphane, library, dahil eder
# import, consults a different library into your code

# if we want to use functions (def) of another library
# we need to import them into our code using "import ..."

mylist = [
	29,32,24,25,21,11,34,35,35,35,35,35,39,23,23,26,
	23,32,33,31,30,12,14,15,16,10,30,27,26,26,26,26,
	33,32,34,30,35,33,17,10,19,22,23,25,27,29,54,45,
	12,35,45,66,78,23,23,34,45,30,30,30,33,33,34,35,
	78,79,70,71,83,84,88,87,89,90,91,87,86,84,83,88,
	99,67,78,89,69,60,80,80,80
]

mylist2 = [
	30, 30, 31, 32, 29, 28, 26, 29, 32, 32, 34, 30, 30, 31,
	29, 32, 28, 26, 25, 29, 30, 33, 33, 32, 99
]

mylist3 = [ # salary
	2500, 2800, 3000, 3000, 2750, 3500,  # [2000 employee]
	45000, # CEO --> exclude !!
]


EMPLOYEE = [2500, 2800, 3000, 3000, 2750, 3500 ]
C_LEVEL = [45000, 35000, 25000]

mylist = np.array( mylist )
mylist2 = np.array( mylist2 )

# mylist = [ 'Ahmet', 'Mehmet' ]

# np.array =~ list 
# numpy array is a kind of list

#: Type of the mylist variable, which is ==> np.array
print(type(mylist))


avg = lambda l: sum(l) / len(l)


# print(avg(mylist))

def getInformation( mylist: np.array ) -> dict:
	stats = {}

	stats[ 'mean' ] = round(np.mean(mylist), 3)
	stats[ 'std' ] = round( np.std(mylist), 3)
	stats[ 'dev' ] = round( stats['std'] / stats['mean'], 3)
	stats[ 'max' ] = np.max( mylist )
	stats[ 'min' ] = np.min( mylist )
	stats[ 'count' ] = len( mylist )
	stats[ 'range' ] = stats['max'] - stats['min']
	stats[ 'mean+std' ] = round(stats['mean'] + stats['std'], 3)
	stats[ 'mean-std' ] = round(stats['mean'] - stats['std'], 3)
	stats[ '#inrange1' ] = len( mylist[ (mylist > stats['mean-std']) & (mylist < stats['mean+std']) ] )
	stats[ '%inrange1' ] = round(stats[ '#inrange1' ] / stats['count'], 3)

	return stats

#! mylist[ mylist > 0 ] # ==> Select * FROM mylist where value > 0

print( getInformation( mylist2 ) )

# Bring the the items from mylist such that the 
# values are greater than mean-std and less than mean+std

# 
"""
SELECT * 
FROM mylist
WHERE value > (mean-std)
AND
value < (mean+std)
"""

# print( mylist[ (mylist > stats['mean-std']) & (mylist < stats['mean+std']) ] ) # filters the data
# inrange = len( mylist[ (mylist > stats['mean-std']) & (mylist < stats['mean+std']) ] )


info = getInformation( mylist2 )
print(info)

# FIRST APPROACH, some statisticans say that
ub = info['mean'] + info['std'] * 3 # upper bound
lb = info['mean'] - info['std'] * 3 # lower bound

print(ub, lb)


plt.hist( mylist2 )
plt.show()



