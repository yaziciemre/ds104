


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


print(oku(1))
print(oku(7))
print(oku(9))
print(oku(63))
print(oku(70))
print(oku(350))
print(oku(1453))


