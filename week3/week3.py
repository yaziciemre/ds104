
# Sualler from last week

# Lambda Function: unique
# Makes a list of values unique
unique = lambda inp: list(set(inp))




def jaccard( a: list, b: list ) -> float:

	a = list(set(a))
	b = list(set(b))

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


x = ['a', 'b', 'c', 'd']
y = ['a', 'b', 'c', 'd', 'a']

# How to make a list "unique"
# We know that "SET" has unique items

# Convert ==> type(  )

q = int(3.5)  # This converts a float (3.5) into integer

#x = list( set( x ) )  #{'a', 'b', 'c', 'd'}
#y = list( set( y ) )

print( "y", y )
print( "set(y)", set(y) )
print( "list(set(y))", list(set(y)) )


# NOTE, in "SETS" there cannot be same item more than once!!

print( jaccard( x, y ) )

print(unique(['a','b','c','d', 'c', 'c', 'c']))





