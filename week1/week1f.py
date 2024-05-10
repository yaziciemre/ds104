










def load_data2( fileName: str ):
	pass

def loadData( fileName: str ):
	# load data from somewhere
	# ...
	pass




temperature = 23.0
temperature = 23



def encrypt( text: str ) -> str :
	return text[::-1]



print( encrypt("SALAM") )







def fToC( f: float ) -> float:
	return (f - 32.0) / 1.8

def convert( convertTo: str, azn: float ) -> float:

	ratio = 1.0
	if convertTo == 'USD':
		ratio = 1.70
	elif convertTo == 'TRY':
		ratio = 1./18.98
	elif convertTo == 'EUR':
		ratio = 1.60
	else:
		raise InvalidValue('error: the given currency is not known' + convertTo)

	return azn / ratio





score = 81

if score > 90:
	grade = 'AA'


elif score > 80:
	grade = 'A'

elif score > 70:
	grade = 'B'

elif score > 50:
	grade = 'C'
else:
	grade = 'F'




print( convert('TRY', 100 ))
print( convert('EUR', 100 ))
print( convert('USD', 100 ))




inchToCm2 = lambda inch: inch * 2.54

def inchToCm( inch: float ) -> float:
	return 2.54 * inch




def squarepower( number: int ) -> int:
	return number * number

squarepower2 = lambda number: number * number

print(squarepower(9))



# =============

import math

print(math.ceil(3.4))
print(math.floor(3.8))
print(round(3.1415, 3))

# =============

a = [40,42,45,60,75,80,61,52,70,99, 0, 33, 39]
b = []

for i in a: # [:10] 
	celcius = fToC(i)
	if i > 40:
		b.append( round(celcius, 2) )


print(a)
print(b)




d = []
for i in a:
	if i > 40:
		d.append( fToC(i) )




c = [fToC(i) for i in a if i > 40.0] # return me a list of items' celcius which are greater than 40
print("a", a)
print("c", c)



# =======================

aa = [i for i in a if i > 40.0]
c = [fToC(i) for i in aa] # return me a list of items' celcius which are greater than 40



# Data Type Conversion
x = 3
y = "3"



str
int
float
bool
list
dict



# 3 ==> 3.0   int ==> float
print( float(3) )

# 3 ==> "3"   int ==> str
print( str(3), type(str(3)) )

# True ==> 1  bool ==> int
print(int(True), int(False))

# 3.5 ==> 3    float ==> int
print(int(3.5))

# "5" ==> 5   str ==> int
print(int("5"))

# "Emre" ==> ['E', 'm', 'r', 'e']    str ==> list
print(list("Emre"))

print('=============')
print(str(True), type(str(True)))
print(True, type(True))



print('=============')



def oku( sayi: int ) -> str:
	...



oku( 1453 ) == "bin dort yuz elli uc"
oku( 1 ) == "bir"
oku( 426 ) == "dort yuz yirmi alti"










	# return multiple values
	# sys.exit(1)
	# recursive
	# if any(ext in email.split('@')[1] for ext in ['_', '-'] ):








#def fToC( f: float ) -> float:
#	return (f - 32.0) / 1.8

#fToC2 = lambda f: (f - 32.0) / 1.8
