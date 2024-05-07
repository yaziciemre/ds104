

# ATOMIC DATA TYPES
a = 3 # Integer, Tam sayi
b = 3.14 # float, ondalikli sayi, decimal
c = True # bool
d = False # bool
e = "Ahmet" # string, text, metin
k = 'Ahmet' # string


# RECOMMENDATION
# NOTE: If you are using a "text data"  use  (double) "
# NOTE: If you are using a constant use (single) '


# COMPLEX DATA TYPES
f = ["Python", "SQL", "PowerBI"] # List of items, values, variables
f = []
f = ['Football']
f = ['xx', 'yy', 'zz', 'tt', 'mm', 'ss']
# -- the length may change
# -- the index (sort) is important
# ['Python', 'SQL'] != ['SQL', 'Python']



g = { # Dictionary of Key = Value
	'TOEFL': 90,
	'Math': 78,
	'Engineering': 95
}
# -- consists of key = value pairs
# -- the length may change
# -- the index ( sort ) IS NOT IMPORTANT (cannot rely on it)
g = {}
g = {'x': 'y'}
g = {
	'Sunday': 0,
	'Monday': 1,
	'Tuesday': 2,


}

g2 = {
	0: 'Ahmet',
	1: 'Mehmet',
	2: 'Ali'
}



h = {'Ahmet', 'Mehmet', 'Mustafa'} #! 'Mehmet', Set


i = ('Mustafa', 28) # Tuple
j = ('Ahmet', 29) # Tuple
# ('Ahmet', 29) != (29,'Ahmet')
# -- Length May NOT CHANGE
# -- the index (sort) is important


k = [] # List of items
k = ['Ahmet', 'Ali']
k = [1, 2, 3]
k = [3.14, 6.78]


k = [ 
	('Ahmet', 28), 
	('Mehmet', 29),
	('Sevda', 21),
	('Zeynep', 22)
]

m = ('Zeynep', 'Female', 22, 'Baku')


k = [

	[ 'Python', 'PowerBI', 'SQL' ],
	[ 'Adobe Photoshop', 'Illustrator'],
	[ 'C#', 'MsSQL']


]


Talebeler = [
	('Zeynep',22,'Female'),
	('Ahmet',29,'Male'),
	('Sevda',21,'Female'),
	('Anar',93,'Male')
]


Talebe = {
	'Name': 'Ahmet',
	'Age': 29,
	'Skillset': ['Python', 'SQL', 'PowerBI'],
	'Gender': 'Male',
	'Address': {
		'City': 'Baku',
		'Street': 'Nizami',
		'Number': 14
	}
}


# y = f(x)
# y = f(x1, x2)


# ===============================================================
# ===============================================================
# ===============================================================

f = [] 
f.append('Ahmet')
f.append('Ali')
f.append('Mustafa')
f.append('Zeynep')
f.append('Heydar')

print("Original List", f)

f.remove('Heydar')

print("Removed list", f)


a = f[ 0 ] # READ, right side of the "Equals sign"
print("f[0]", a)

print( "f[0] direct", f[0] )


f[0] = "Ayse" # WRITE, left side of the "Equals sign"

print("Changed list", f)


print("Length of list", len(f))

print("Length of Muhammed", len("Muhammed"))


print('============')


print("a", "b", "c", "d")


print('============')

print("Original List", f)
print("Original List", "f")


print('============')

Talebe = {
	'Name': 'Ahmet',
	'Age': 29,
	'Skillset': ['Python', 'SQL', 'PowerBI'],
	'Gender': 'Male',
	'Address': {
		'City': 'Baku',
		'Street': 'Nizami',
		'Number': 14
	}
}



x = Talebe['Gender']
print("Bizim Talebe", Talebe)
print("Talebenin gender", x)

x = Talebe['Skillset'][1]
print( "Talebenin 1. inci skilli", x )






a = {'math': 94, 'english': 80, 'art': 37, 'statistics': 70}
b = ['Python', 'SQL']
c = ('Mustafa', 22)

print(a['math'])
print(b[1])
print(c[0])


keylist = list(a.keys())
print("keylist", keylist)
print(keylist[0])
print(a.values())




Talebe = {
	'Name': 'Ahmet',
	'Age': 29,
	'Skillset': ['Python', 'SQL', 'PowerBI'],
	'Gender': 'Male',
	'Address': {
		'City': 'Baku',
		'Street': 'Nizami',
		'Number': 14
	},
	'Grades':{
		'Math': 90,
		'Science': 60,
		'Litreature': 80,
		'Art': 75
	}
}


city = Talebe['Address']['City']
print(city)
print(Talebe['Grades']['Math'])
print(Talebe['Grades'].keys())
print(Talebe['Grades']['Science'])

Talebe['Grades']







YeniTalebe = {
	'Name': 'Ahmet',
	'Grades':
	[
		{'Course': 'Math', 'Score': 90},
		{'Course': 'Science', 'Score': 60},
		{'Course': 'Litreature', 'Score': 80},
		{'Course': 'Art', 'Score': 75},
	]

}


print(YeniTalebe['Grades'][0]['Course'])



Talebeler = [
	{'Name': 'Zeynep', 'R': 5, 'I': 5},
	{'Name': 'Ayten', 'R': 6, 'I': 4},
	{'Name': 'Semra', 'R': 4, 'I': 7},
]


Talebeler2 = {
	'Zeynep': {'R': 5, 'I': 5},
	'Ayten': {'R': 6, 'I': 4},
	'Semra': {'R': 4, 'I': 7},
}

print(Talebeler[0]['I'])
print(Talebeler2['Ayten']['I'])

print( len("AZ") )
print( len( ['Ahmet', 'Veli'] )  )
print( len( {'Math': 90, 'Science': 80} )  )
print( len( ('Ahmet', 33) )  )


# len() ==> method
# ('Ahmet', 28) ==> tuple

# a = [] ==> List creation
# a[3]   ==> List item reach


# ====================
i = 3
s = "Emre"
p = ['E', 'm', 'r', 'e']

print(s[2], p[2])


print('================================')
print('================================')
print('================================')
print('================================')
print('')




f = [] 
f.append('Ahmet')
f.append('Ali')
f.append('Mustafa')
f.append('Zeynep')
f.append('Heydar')


# THESE FUNCTIONS (indexer) DO NOT MODIFY THE ORIGINAL "f" variable

print(f, f[1:3])  # From 1 to (exclude) 3
print(f, f[-1])   # Last one
print(f, f[:3])   # From Zero to (exclude) 3
print(f, f[1:])   # From 1 to Last
print(f, f[1:-1]) # Skip the first and last
print(f, f[-2:])  # Last two items
print(f, f[:])    # Same
print(f, f[::-1]) # Reverse



print(f[1:3], f)  # From 1 to (exclude) 3
print(f[-1], f)   # Last one
print(f[:3], f)   # From Zero to (exclude) 3
print(f[1:], f)   # From 1 to Last
print(f[1:-1], f) # Skip the first and last
print(f[-2:], f)  # Last two items
print(f[:], f)    # Same
print(f[::-1], f) # Reverse


print("==========================")

# THESE FUNCTIONS MODIFY THE ORIGINAL "f" VARIABLE


f.reverse() # f is changed!!!!!
print(f)


print( f.pop() ) # RETURN THE LAST ITEM, AND REMOVE IT FORM LIST

print( f.pop(0)) # RETURN THE FIRST ITEM, AND REMOVE IT FROM LIST




s = "Emre"

print(s[1:3])


mysalary1 = "1000 AZN"
mysalary2 = "1000AZN"

mysalary1 = mysalary1.strip()


print(mysalary1[:-3])
print(mysalary2[:-3])


# What is your occupation
# doctor
# Doctor
# Doctor__
# Dr.
# dr
# dr..
# prof. dr
# professor doctor



occupations = [
	'Doctor',
	'doctor',
	'Doctor  ',
	' Doctor',
	' Doctor ',
	'Dr.',
	'Dr',
	'dr',
	'dR.'

]


KISALTMA = {
	'eng': 'engineer',
	'doc': 'doctor',
	'dr': 'doctor',
	'prof': 'professor',
	'av': 'avukat'
}

for salam in occupations:

	changed = salam # create a new variable with the value of "salam"
	changed = changed.lower()  # dr.
	changed = changed.strip() 
	changed = changed.replace(".", "") # dr

	if changed in KISALTMA:
		changed = KISALTMA[ changed ]    # KISALTMA[ 'dr' ]
	print(salam, "===>", changed)


# Email checking
public = [
	'gmail.com',
	'yandex.ru',
	'msn.com',
	'yahoo.com',
	'icloud.com',
	'mail.ru',
	'mail.com',
]

email1 = "ahmetyunsel@gmail.com"
email2 = "yunahmet@minapy.com.tr"
i1 = email1.strip().index('@')
i2 = email2.strip().index('@')

if email1[ i1+1: ] in public:
	print('email1 bir PUBLIC email adresidir')
else:
	print('email1 bir SIRKET email adresidir')

if email2[ i2+1: ] in public:
	print('email2 bir PUBLIC email adresidir')
else:
	print('email2 bir SIRKET email adresidir')




print( email1.split("@")[-1] )
print( email2.split("@")[1] )



a = email1.split('@')[1] in public

print(a)




