
invalid_emails = [
    "plainaddress",
    "@missingusername.com",
    "username@.com.my",
    "username@.com",
    "username@.com.com",
    "username@-example.com",
    "username@111.222.333.44444",
    "username@example",
    "username@example..com",
    "username@example.com (Joe Smith)",
    "username@example",
    "username@.invalid",
    "username@%*.com",
    "username..email@example.com",
    "username.@example.com",
    "username@.com.",
    "username@-example.com",
    "username@example.web",
    "username@.com@",
    "username@example#archive.com",
    "username@example#@com",
    "username@.org",
    "username@*.com",
    ".username@example.com",
    "username@.com.",
    "username@example.com.",
    "username@example..com",
    "username@..example.com",
    "username@example.com (extra text)",
    "username@example.com Joe Smith",
    "username example.com",
    "username@example,com",
    "username@exa mple.com",
    "username@exam_ple.com",
    "user name@example.com",
    "username@ex*ample.com",
    "username@exa(mple.com",
    "username@exa)mple.com",
    "username@exam=ple.com",
    "username@",
    "user@.com",
    "@example.com",
    "email.@example.com",
    "email..email@example.com",
    "あいうえお@example.com",
    "email@example.com (Joe Smith)",
    "email@example",
    "email@111.222.333.44444",
    "email@example..com",
    "username@example..com"
]

valid_emails = [
    "sarnot0@devhub.com",
    "schristoffels1@earthlink.net",
    "gnoads2@miibeian.gov.cn",
    "olowdyane3@imgur.com",
    "bleipelt4@ask.com",
    "cthebe5@globo.com",
    "gmcnern6@themeforest.net",
    "fturnbull7@dropbox.com",
    "lgallier8@biglobe.ne.jp",
    "aoshevlan9@facebook.com",
    "rdorkensa@i2i.jp",
    "imortonb@noaa.gov",
    "sbecceroc@ucoz.ru",
    "hcrichmered@wikimedia.org",
    "bblowese@cbslocal.com",
    "wniesef@list-manage.com",
    "smyringg@google.it",
    "tmacilwrickh@alibaba.com",
    "sbrunskilli@dyndns.org",
    "ckingstnej@go.com",
    "seagerk@surveymonkey.com",
    "bteaguel@icq.com",
    "glardgem@goo.ne.jp",
    "kgepheartn@e-recht24.de",
    "vbono@w3.org",
    "bsimonnetp@privacy.gov.au",
    "shierroq@imageshack.us",
    "nlidgettr@dion.ne.jp",
    "rseifenmachers@craigslist.org",
    "eisaqt@photobucket.com",
    "vstreetsu@hugedomains.com",
    "btrewhellav@engadget.com",
    "fclucasw@pagesperso-orange.fr",
    "ependdrethx@zimbio.com",
    "cbossony@nymag.com",
    "pcrozierz@yellowpages.com",
    "ccoveley10@blogtalkradio.com",
    "hbruyns11@php.net",
    "mvella12@clickbank.net",
    "jberan13@jimdo.com",
    "jkinge14@accuweather.com",
    "lbinfield15@wikimedia.org",
    "ndugood16@ehow.com",
    "acurteis17@rambler.ru",
    "kfishburn18@skype.com",
    "aleeder19@princeton.edu",
    "gmacconnechie1a@cdbaby.com",
    "jwashbrook1b@tinyurl.com",
    "dglisane1c@stanford.edu",
    "crichens1d@prweb.com"
]



def score( function ):

	correct = 0
	invalids = 0
	valids = 0
	for i in invalid_emails:
		if function( i ) == False:
			correct = correct + 1
			invalids += 1

	for i in valid_emails:
		if function( i ) == True:
			correct = correct + 1
			valids += 1
	
	return correct #, invalids, valids


# =============================================
# =============================================
# =============================================
# =============================================
# =============================================
def Zaren(email):
    forbidden_char = [ '!','?','$','%', '#', '$', ',' ] #list of special characters
    for i in forbidden_char:
        if i in email:
            return False
 
    if '@' not in email or '.' not in email:
        return False
    if email.count("@")>1:
        return False
    if  email[-1] == '@' or email[-1] == '.':
        return False
    if  email[0] == '@' or email[-1] == '.':
        return False
    if len(email)<10:
        return False
    else:
        return True
#main part             


# =============================================


allowed_characters_for_first_part = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!$%^&*_=+}{'?-.")
allowed_characters_for_second_part = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
special_characters_first_part = set("~!$%^&*_=+}{'?-.")
special_characters_second_part = set("-.")


def Gultaj( email ):
	
    # @ check
	if len(email) < 10: return False # must have at least 10 characters long
	if '@' not in email: return False # must contain @ 
	if email.count('@') > 1: return False # must contain no more than one @
	if email[0] == '@' or email[-1] == '@': return False # @ must not be first or last character
	
    # splitting email into first and second part 
	first_part, second_part = email.split("@")
	
    # second part check 
	
	if '.' not in second_part: return False # second part must contain '.'
	
    # 1 allowed characters
	for char in second_part: 
		if char not in allowed_characters_for_second_part: return False
		
    # 2 '.' and '-' cant be first or last characters 
	if second_part[0] in special_characters_second_part or second_part[-1] in special_characters_second_part:
		return False
	
    # 2 '.' and '-' cant be consecutive 
	for i in range(len(second_part) - 1):
		if second_part[i] in special_characters_second_part and second_part[i + 1] in special_characters_second_part:
			return False
	

    # first part check
	
    # 1 allowed characters 
	for char in first_part: 
		if char not in allowed_characters_for_first_part: return False	
		
    # 2 special characters cant be consecutive 
	for i in range(len(first_part) - 1):
		if first_part[i] in special_characters_first_part and first_part[i + 1] in special_characters_first_part:
			return False
		
    # 3 special characters cant be first or last characters 
	if first_part[0] in special_characters_first_part or first_part[-1] in special_characters_first_part:
		return False
	return True

# =============================================

SPECICAL_CHARS_2 = ['!','&','?','$','%',';',':','#','*','=','^',',']

def Suleyman( email ):

	if len(email) < 10: return False
	if '@' not in email: return False
	if '.' not in email: return False
	if email[0]=='@' or email[0]=='.': return False
	if email.count('@')>1 : return False
	if '@' in email and len(email.split('@')[1]) == 0:return False
	if email[len(email)-1]=='.':return False
	if ' ' in email: return False
	for c in SPECICAL_CHARS_2:
		if c in email:
			return False
	for i in range(len(email)-1):
		if email[i]=='.' and email[i]==email[i+1]:
			return False
	for i in range(len(email)-1):
		if email[i]=='@' and ( email[i+1]=='.' or email[i-1]=='.' ):
			return False
	for i in range(len(email)-1):
		if email[i]=='@' and ( email[i+1]=='-' or email[i-1]=='-' ):
			return False
	for i in range(len(email)-1):
		if email[i]=='@' and ( email[i+1]=='_' or email[i-1]=='_' ):
			return False


	return True


# =============================================




SPECICAL_CHARS = [ # bu karakterlerden herhangi biri varsa!
'!',
'?',
'$',
'%',
'&',
'-',
'+',
'=',
',',
'/',
':',
';',
':',
'~',
'*',
'^',
'>',
'<',
'#',
')',
'('
]

DOMAIN_LIST = [ # @den sonrasinin duzgunluyunu yoxlamaqcun
	'com',
	'mail',
	'email',
	'gmail',
	'yandex',
	'yahoo',
	'outlook',
	'hotmail',
	'edu',
	'gov',
	'org',
	'mil',
	'net',
	'biz',
	'ru',
	'bk',
	'tr',
	'az'
]


def Turkan(email):
	if len(email)<10:
		return False
	if '@' not in email:
		return False
	if '.' not in email:
		return False
	if ' ' in email:
		return False
	for c in SPECICAL_CHARS:
		if c in email:
			return False
	if email.count('@')	>1:
		return False
	if '@' in email and len(email.split('@')[1]) == 0:
		return False
	if '@' in email and len(email.split('@')[0]) == 0:
		return False
	

	if '.' in email and len(email.split('.')[0]) == 0:
		return False
	if '.' in email and len(email.split('.')[0]) == 0:
		return False
	if '.' not in email.split('@')[1]:  # @-den sonraki hissede noqte yoxdursa
		return False


	if email.index('@') == email.index('.') + 1:  # .@ yazilarsa
		return False
	if email.index('.') == email.index('@') + 1:  # @. yazilarsa
		return False
	


	parts = email.split('@')        # domain ve ext hisselerine bolub domain listde duzgunluyunu yoxlayiriq
	domain = parts[1].split('.')[0]
	extension = parts[1].split('.')[1]
	if extension not in DOMAIN_LIST:
		return False

	return True


# =====================================

Special_char = ['!', '#', '$', '%', '&', '*',
                '+', '-', '/', '=', '?', '^',
                '_', '`', '{', '|', '}', '~',
                '-', '"', '(', ')', ',', ':'
                ';','<', '>']

def Tabrik(email):
    for i in Special_char:
        if i in email:
            return False
    if len(email) < 10: 
        return False
        
    if '@' not in email:
        return False
    if '@' in email[0] and email[-1]:   # @ not first or last character
        return False
    if email.count('@') > 1:
        return False 
    if '.' not in email:
        return False
    if '.' in email[0] and email[-1]:   # '.' not first or last character 
        return False
    for i in email:
        if i.isupper():   # Capital Letter 
            return False
    if '.' in email.split('@')[1]  == 0: # dont have '.' from '@'
        return False

    
    
    return True



SPECIAL_CHARS3 = ['!','?','$','%','&','*','+','/','=','#','^','`','{','}','|','~','[',']','(',')',',',';',':','<','>','\"','\'']
NUMBERS=['0','1','2','3','4','5','6','7','8','9']
def Samra(email):
	if len(email) < 10: return False # sayi az olmasin
	if '.' not in email: return False #eger . yoxdursa yanlisdir
	if email.count('@') != 1: return False # sadece bir "@" işareti olmalı
	if ('..') in email: return False#.. olmaz
	if ('.@') in email: return False
	if email[-1] == '.' or email[-1] == '@': return False #sonda noqte ve @ olmamalidir
	if '@' in email and len(email.split('@')[0]) == 0: return False
	if '@' in email and len(email.split('@')[1]) == 0: return False
	if '.' in email.split('@')[1][-1]: return False
	if '.' in email.split('@')[0]: return False
	if '_' in email.split('@')[1]: return False #neden or ya yazamiyoruz '-' ve '_'
	if '-' in email.split('@')[1]: return False
	#ingilizce karakterler regex le yaziliyormus baktim ama eklemedim. yani turkce veya cince ekleyemezsin.
	for c in SPECIAL_CHARS3:
		if c in email: 
			return False
	for n in NUMBERS:
		if n in email.split('@')[1]: 
			return False
	return True


	# if any(ext in email.split('@')[1] for ext in ['_', '-'] ):


def Ayten(email):
  email=email.strip()
  splitted1=email.split("@")
  splitted2=email.split(".") 
  common=splitted1+splitted2 

  if '@' not in email: return False
  if '.' not in email: return False
  if email=="" or \
    email.count(" ")>=1 or \
    email.count("@")!=1 or \
    len(email)<8 or\
    (email.index("@")>email.index(".")) or (email[0]=="@") or \
    len(splitted2[-1])<2 or \
    email[0].isdigit()==True or \
    email!=email.lower() or\
    len(splitted1[-1])<5 :
    return False
  return True




print( "Zaren", score( Zaren ) )
print( "Gultaj", score( Gultaj ) )
print( "Suleyman", score( Suleyman ) )
print( "Tabrik", score( Tabrik ) )
print( "Turkan", score( Turkan ) )
print( "Samra", score( Samra ) )
print( "Ayten", score( Ayten ) )






