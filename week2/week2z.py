



def jaccard( a: list, b: list ) -> float:

	# number of (count of) common items in both a and b
	nof_common = 0
	# total items both in a and b - nof_common
	total_items = 0
	# Check	
	for i in b: # append to all items, whatever in list b
		if i in a:
			nof_common = nof_common + 1
	
	total_items = len(a) + len(b) - nof_common

	
	return nof_common / total_items


def jaccard_version2( a: list, b: list ) -> float:

	# number of (count of) common items in both a and b
	nof_common = 0
	# Check	
	for i in b: # append to all items, whatever in list b
		if i in a:
			nof_common += 1
	
	return nof_common / (len(a) + len(b) - nof_common)


def jaccard_version3( a: list, b: list ) -> float:
	nof_common = len([i for i in a if i in b])
	# give me number of items in "a" if they are already in "b"
	return nof_common / (len(a) + len(b) - nof_common)



	


footballteam =   ['Ahmet', 'Mustafa', 'Ali', 'Haydar' ] # list of items
basketballteam = ['Ahmet', 'Emir', 'Anar', 'Ali', 'Farid'] # list of items
swimmingteam =   ['Ahmet', 'Emir', 'Anar', 'Mehmet'] # list of items
volleyballteam = ['Musa', 'Zeyneb', 'Semra']


# NOTE: if we are going to use a variable ONCE, 
# after we use it, we can overwrite


# declare (Hey python, there is a variable called result)
# assignment (Hey python, the value of "result" is calculated with jaccard)
result = jaccard( footballteam, basketballteam )
# get/read (Hey python, give me the value of result)
print('similarity of footballteam, basketballteam', result)



# this statement below, CHANGES / UPDATES / OVERWRITES the result!
result = jaccard( basketballteam, footballteam )
print('similarity of basketballteam, footballteam', result)

result3 = jaccard( footballteam, swimmingteam )
print('similarity of footballteam, swimmingteam', result3)

result4 = jaccard( basketballteam, swimmingteam )
print('similarity of basketballteam, swimmingteam', result4)

result = jaccard( volleyballteam, swimmingteam )
print('similarity of volleyballteam, swimmingteam', result)

result = jaccard( volleyballteam, volleyballteam )
print('similarity of volleyballteam, volleyballteam', result)



"""
a = [x, y]
b = [x, y, z]

[x, y]

   2
-----------    2 / 3 == 0.66...
   2+3-2
"""


# multiplication of items from 1 to n
def factorial( n: int ) -> int:
	result = 1
	for i in range(n):
		result = result * (i+1)
	return result

#0,1,2,3,4....n-1



"""
3! = 3 x 2 x 1
n! = n x (n-1) x (n-2) x ..... x 1
2! = 2 x 1
1! = 1
0! = 1
12! = 12 x 11 .....
12! = 12 x 11!
2! = (2) x (2-1)!

10! = 10 x (10-1)!
n! = n x (n-1)!
"""