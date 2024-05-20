
import re # regular expression | pattern | template

# regex helps us to correct, incorrectly written user input

# qiymet list
q = [
	"  17,06 AZN",
	"21 AZN",
	"72AZN",
	"29,06AZN",
	" 30azn",
	"40.04 AZn",
	"50",
	"coq"
]


# [a-zA-Z0-9\_]

email = r"[a-zA-Z0-9\_\.]+@[a-zA-Z0-9]+\.[a-zA-Z]+"
name = r"^[A-Z][a-z]+$"
abbreviation = r"^[A-Z][a-z]+\.$"
measurement = r"^[0-9]+\.[0-9]+\s[a-z]+$"
decimal = r"[0-9]+(\.[0-9]+)?"
email_with_country = r"[a-z]+@[a-z]+\.[a-z]+(\.[a-z]+)?"
url = r"(http\:\/\/)?[a-z]+\.[a-z]+(\.[a-z]+)?"
date = r"^[0-9]?[0-9][\.\-\/][0-9]?[0-9][\.\-\/][12][0-9]([0-9][0-9])?$"

# in regex
# [a-z] --> means, one of them inside
# [\.\-\/]
# . - /


# registration plate
# postal code
# address
# email
# url
# time
# date
# name
# abbrevation
# numbers
# currencies




for i in q:
	i = i.strip()
	i = i.lower()
	i = i.replace("azn", "")
	i = i.strip()

	# + ===> 1 or more than once

	if re.match(r"^[0-9]+([\,\.][0-9]+)?$", i):
		print(i, "matches", "float")
	else:
		print(i, "NOT MATCHES")



