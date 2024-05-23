
SELECT Name # only return the "name" column
FROM Students
WHERE Age = '28' # only with age 28
ORDER BY Name; # sorted

SELECT DISTINCT Name # Distinct ==> unique
FROM Table
WHERE Age = '28'
ORDER BY Name; # <---------- at the end

# In sql, there is no limitation to use "new line"
SELECT DISTINCT Name FROM Table WHERE Age = '28' ORDER BY Name;

SELECT DISTINCT Name 
FROM Table WHERE Age = '28' ORDER BY Name;

SELECT DISTINCT Name 
FROM Table 
WHERE Age = '28' 
ORDER BY Name;

# To eliminate/ignore duplicate items, we use Distinct

a = ['Ahmet', 'Ali', 'Mehmet', 'Anar', 'Ali']
a = list(set(a)) # unique - distinct

	a = ['Ahmet','Mehmet', 'Anar', 'Ali']


# Bir nefer Kaza yapti mi yapmadi mi?
# Kac kere yaptigi onemli degil!

SELECT DISTINCT Plate
FROM Accidents
# The vehicles which have accidents
# BOOL (true or false, has the car ever made an accident, regardless of count)

/* comment */
# comment --> just like in python, it is a single line comment

/* multi line comment
 * select items from table ..... [some description]
 * 
 */

SELECT *
FROM Accidents
WHERE Country = 'Azerbaycan' AND Plate LIKE '77%';
# In python, to match a string with pattern, template ==> regex


SELECT *
FROM Accidents
WHERE Country = 'Azerbaycan' AND 
(
	Plate LIKE '77%'
	OR
	Plate LIKE '90%'
	OR
	Plate LIKE '99%'
	OR
	Plate LIKE '10%'
); # Baku registration plates, in Azerbaycan


SELECT *
FROM Accidents
WHERE Country = 'Turkiye' AND Plate LIKE '77%' # ==> YALOVA


# The vehicles which have accidents, which are not from Baku
SELECT *
FROM Accidents
WHERE Country = 'Azerbaycan' AND NOT
(
	Plate LIKE '77%'
	OR
	Plate LIKE '90%'
	OR
	Plate LIKE '99%'
	OR
	Plate LIKE '10%'
); # Baku registration plates, in Azerbaycan


# NOT
SELECT * FROM Customers
WHERE NOT Country = 'Spain';

# NOT
SELECT * FROM Customers
WHERE Country <> 'Spain';


# Bring me the Nefers from nefer table, who are not attended to a university
SELECT Name, Surname
FROM Nefer
WHERE University IS NULL;  #  Never Assigned


SELECT Name, Surname
FROM Nefer
WHERE University = ''; # Empty


Python
a = '' # empty string
a = None # bunun memory de bir yeri YOK!!

INSERT INTO Nefer (Name, Surname, University)
	VALUES ('Ali', 'Yilmaz', 'Baku Economics University' );

INSERT INTO Nefer (Name, Surname, University)
	VALUES ('Ahmet', 'Yildiz', '' );

INSERT INTO Nefer (Name, Surname)
	VALUES ('Mustafa', 'Kaya' );

INSERT INTO Nefer (Name, Surname, University)
	VALUES ('Mustafa', 'Kaya', NULL );


# Universitesi olan neferleri getir
# In most cases, we may need to use some variables, so, we discard which are NONE (empty)
SELECT Name, Surname
FROM Nefer
WHERE University IS NOT NULL;


# You have started working in google
# First day
SELECT * 
FROM RECORDS
# You will get fired
# 30 yil 
# CPU %100
# HARDDISK = FAIL

10 trilyar records


# SQL Server
SELECT TOP 100 * FROM RECORDS

# MySQL
SELECT * FROM RECORDS LIMIT 0, 100

# Sampling ! , data science

# Take a look at the data, what is in it?

# if there are 30 records in db => 30 
# if there are 100 records in db => 100
# if there are 100000 records in db => 100

# Bring me the salaries of the persons in company
SELECT Salary
FROM Employees

# Bring me the maximum salary
SELECT Max(Salary)
FROM Employees

SELECT Min(Salary)
FROM Employees

SELECT Max(Salary), Min(Salary)
FROM Employees
12000 1000

SELECT Avg(Salary)
FROM Employees

# BOSS: How much salary I am paying to my employees 
SELECT SUM(Salary)
FROM Employees

# Pay raise, incremention

# Python
if a in ['Germany', 'Spain', 'UK']:
	pass

# Bring me the tourists who are NOT from Europe
SELECT * FROM
Tourists
WHERE Country NOT IN ('Germany', 'Spain', 'UK');

# Interview applications for job post
# Bring me only the people whose age between 20 and 40
SELECT * FROM
Candidates
WHERE Age BETWEEN 20 AND 40


Age => Sayisal numeric
Salary => Sayisal numeric
NEVER USE quote ''

The values which have digits, but they are NOT numeric
- date
- FIN NUMBER
- Phone Number     341749422
- Student Number
- Plate ==> city


int tanimlariz!! 

10 	Baku
11 	Beyləqan

# INCORRECT,  Beylakan bakuden buyuktur, WRONG, ABSURD
Beyləqan - Baku = 1
Beyləqan - Baku =  birbirine cok benzer


			  int
Ahmet Salary  3000
Mehmet Salary 3050

STATEMENT: Ahmetin salarysi MEhmetin salarysine cok benzer, cok yakin

3050-3000 MANTIKLI - LOGICAL
STATEMENT: The difference between Salaries of Ahmet and Mehmet is only 50


STATEMENT: Baku ile Beyləqan arasindaki fark 1 ???? !!!! !?!#@$#@$!$@!$@


            int
Person		Car Plate City
Ahmet       10


In numeric value we can do the following
Max, Min, Average
+ - / *
>< 



(Emre YAZICI)        (Nobody, Anybody)
348752985739 + 1 ==  348752985740


CREATE TABLE Students
	Name varchar(50),
	Age varchar(5)
	...



INSERT INTO ....



SELECT CAST(Age as int) FROM Students
# CAST => CONVERT 

In Python
a = '3'
b = 3
c = '4'
d = 4

a + c ==> '34'
b + d ==> 7



e = 'Ahmet'
f = 7

e + f





