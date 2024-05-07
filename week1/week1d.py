









inputs = [
	'eyazici@minapy.com.tr',
	'yaziciemre@gmail.com',
	'yaziciemre@msn.com',
	'emre@yazici',
	'emre.yazici@',
	'emre',
	'e@e.com',
	'@emreyazici.com',
	'emre@@emre.com',
	'emre!@emre.com',
]


SPECICAL_CHARS = [ # bu karakterlerden herhangi biri varsa!
'!',
'?',
'$',
'%'
]


for inp in inputs:
	if '@' not in inp:
		print('@ YOK', inp)

	if '.' not in inp:
		print('NOKTA YOK', inp)

	if '@' in inp and len(inp.split('@')[1]) == 0:
		print('@ ten sonrasi YOK', inp)


	if '@' in inp and len(inp.split('@')[0]) == 0:
		print('@ ten oncesi YOK', inp)

	if len(inp) < 10:
		print('COK KISA', inp)

	if inp.count('@') > 1:
		print('cok fazla @ kullandin')

	for c in SPECICAL_CHARS:
		if c in inp:
			print('illegal karakter kullanildi', inp)






def donustur( inch ):
	return inch * 2.54


print(donustur(100))




def emailDogrumuAyten( email ):

	if len(email) < 10: return False
	if '@' not in email: return False
	if '.' not in email: return False
	for c in SPECICAL_CHARS:
		if c in email:
			return False



	return True


sonuc1 =  emailDogrumu('emreemrererere')
sonuc2 =  emailDogrumu('emre@yazici.com')

print(sonuc1)
print(sonuc2)