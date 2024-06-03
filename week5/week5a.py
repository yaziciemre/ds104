file = "week4_Invistico_Airline.csv"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 00|read_csv:  Load the data in file into a variable called df (dataframe)
df = pd.read_csv(file)

print(df.describe().T)


a = 1
if a == 3: # sart, condition
	print('ok')

a = None
# if not (a == None or a == 0)
# ==> False
# else
# ==> True (3,5,13412340, 1234234)

if a: # In integers, if the given value is not 0 then it is true
	print('ok2')

# the aim is to check a is none, if we have coded this line, that means
# the variable a may have the value of "none"
if a == None:
	pass


# =======================================================
# =======================================================
# =======================================================
# =======================================================
# =======================================================


# Global variales
pi = 3.1415 # Defined in file 
# The default value of pi for ALL codes in this file is 3.1415, default!!!
# oz degeri
# unless it is already defined in a function (as local variable)

def around(radius):
	return pi * 2 * radius

# scope of variables
def area(radius):
	# local variables: defined in a function or class!!!
	global pi  # I am taking this responsibility to change the value of pi
	# all over in python file, so that all other methods using pi
	# may be effected
	pi = 3
	return pi * radius * radius

# ==========================================================

# global variable
task_count = 10
print(task_count)

def printTaskCount():
	# To read value of a global variable, just use it!
	print("Task count" + str(task_count))

def makeTask( name ):
	# aggreement, signed
	global task_count # I know, task_count is a global variable and I want to change it
	print('making this task:', name)
	task_count += 1 # increment the task count

	# NOTE, if I want to change the global variable with in a function
	# WE NEED TO USE "global" keyword



print( area( 10 ) )
# 300
# 314.15


# Constant variables or a variables that is used by more than one function should be defined at the top of the code.

# ======================================

name_regex = r"^[A-ZÇĞİÖŞÜƏ][a-zçğıöşüə]{2,20}+ [A-ZZÇĞİÖŞÜƏ][a-zçğıöşüəA-ZZÇĞİÖŞÜƏ]{2,20}+$"

zeyneb = r"^[A-ZÇĞİÖŞÜƏ][a-zçğıöşüə]{2,20}+ ([A-ZZÇĞİÖŞÜƏ][a-zçğıöşüə]{2,20}+ )?[A-ZZÇĞİÖŞÜƏ][a-zçğıöşüəA-ZZÇĞİÖŞÜƏ]{2,20}+$"
# Muhammed Emin MAMMADZADA
# ? = olabilir, olmayabilir (1/0) var veya yok 1 tane var veya 0 tane var
# .com.tr
# .com
# Muhammed MAMMADZADA

# \w matches any word character (equivalent to [a-zA-Z0-9_])
