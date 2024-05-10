


birlik = {
	'0': '',
	'1': 'bir',
	'2': 'iki',
	'3': 'uc',
	'4': 'dort',
	'5': 'bes',
	'6': 'alti',
	'7': 'yedi',
	'8': 'sekiz',
	'9': 'dokuz',
}

onluk = {
	'0': '',
	'1': 'on',
	'2': 'iyirmi',
	'3': 'otuz',
	'4': 'qirk',
	'5': 'elli',
	'6': 'altmis',
	'7': 'yetmis',
	'8': 'seksen',
	'9': 'doksan',
}


def oku( number: int ) -> str:

	number = str(number)

	if len(number) == 1:
		return birlik[ number ]
	if len(number) == 2:
		return onluk[ number[0] ] + " " + birlik[ number[1] ]
	if len(number) == 3:
		return birlik[ number[0] ] + " yuz " + onluk[ number[1] ] + " " + birlik[ number[2] ]
	if len(number) == 4:
		return birlik[ number[0] ] + " bin " + birlik[ number[1] ] + " yuz " + onluk[ number[2] ] + " " + birlik[ number[3] ]

# eger 1 karakterliyse ==> bir iki uc .....
# eger 2 karakterliyse ==> on yirmi otuz ... + bir iki uc
# eger 3 karakterliyse ==> bir iki uc  + yuz + (2 karakterli) + (1 karakterli)
# eger 4 karakterliyse ==> bir iki uc + bin + bir iki uc + yuz ....


def oku2( number: int ) -> str:

	if number < 10:
		return birlik[ str(number) ]

	if number < 100:

		# 63
		# 63 / 10 = 6.3
		# round(6.3) = 6
		onlar =  int(number / 10)
		
		# 63 - 6 x 10
		birler = number - onlar * 10

		return onluk[ str(onlar) ] + " " + birlik[ str(birler) ]

	if number < 1000:

		# 351
		# 3, 5, 1
		# 
		yuzler = int(number / 100)
		onlar = int((number - yuzler * 100) / 10)
		birler = number - yuzler * 100 - onlar * 10

		return birlik[ str(yuzler) ] + " yuz " + onluk[ str(onlar) ] + " " + birlik[ str(birler) ]



print(oku(1), oku2(1))
print(oku(7), oku2(7))
print(oku(9), oku2(9))
print(oku(63), oku2(63))
print(oku(70), oku2(70))
print(oku(351), oku2(351))
print(oku(1453), oku2(1453))



#pi = 3
#pi = 3.14
#pi = 3.1415
#pi = 22.0/7.0

def areaHesapla( radius: float, pi: float = 3.14 ) -> float:
	return radius * radius * pi

print( areaHesapla( 10 ))
print( areaHesapla( 10, 3.14 ))
print( areaHesapla( 10, 3.1415 ))
print( areaHesapla( 10, 3.14159265359 ))





# Nizami k. 203B, AF Business House, 2-ci mərtəbə



a = {
	'street': 'xyz',
	'city': 'abc',
	'number': 123,
	'town': 'pwr' 
}

# xyz streeti, no:123, pwn/abc



def addressString( info: dict ) -> str:
	



address = {
	'kuce': 'Nizami',
	'number': '203B',
	'city': 'Baku',
	'rayon': 'xyz',
	'qesebe': 'abc'
}

print( addressString( address ) )




