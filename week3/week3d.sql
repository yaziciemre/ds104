


SELECT name, surname, plate_number, accident_date, model
FROM policies
WHERE 
	plate_number = '99 ABC 4325'
	OR
	fin_number = 'FC49832'



WHERE => harada? | Such that


in maths

x = x | x == 2n oyle ki; such that






SELECT *
FROM policies
WHERE `Vehicle Make` = 'Ford'
or
and
between
!= 
not in
in


ELASTIC query language
SQL = Structured Query Langauge 


SELECT [ which columns to select ]
FROM policies
WHERE [ which rows to select ]

Customer Name
John Doe
Jane Smith
Bob Johnson
Alice Brown
Charlie Black
Eve White
Frank Green
Grace Red
Hank Blue
Ivy Gold



SELECT `Vehicle_Make` 
FROM policies

Vehicle Make
Toyota
Honda
Ford
Nissan
Toyota
Honda
Ford
Nissan
Toyota
Honda
...
...
...


Grouping !!!
Excel: Pivot Table
Vehicle Make	Count - Vehicle Make
Ford	2
Honda	3
Nissan	2
Toyota	3


SQL

SELECT `Vehicle Make`, COUNT(*)
FROM policies
GROUP BY `Vehicle Make`

The total number of policies for each Vehicle Make "IN TOTAL!!!"

Vehicle Make	Count
Ford	200
Honda	300
Nissan	250
Toyota	1000

The total number of policies for each Vehicle Make, "SUCH THAT HAS ACCIDENT"
SELECT `Vehicle Make`, COUNT(*)
FROM policies
WHERE Claimed = 'Yes'
GROUP BY `Vehicle Make`

Vehicle Make	Count - Vehicle Make
Ford	170
Toyota	50
Nissan	120
Honda	30

Ford	170 / 200 = %85
Honda	30 / 100 = %10
Nissan 	120 / 250 = %48
Toyota	50 / 1000 = %5







SELECT * 
FROM car
WHERE plate_number = '34 BUY 543'

id 	plate_number
2   34 buy 543


SELECT * 
FROM car
INNER JOIN [join with whom] ON [join how?]
WHERE plate_number = '34 BUY 543'



SELECT * 
FROM car
INNER JOIN accident ON acccident.carid = car.id
WHERE plate_number = '34 BUY 543'

id 	plate_number	date
2   34 buy 543		12.12.2022
2   34 buy 543		05.05.2022
2   34 buy 543		07.12.2000


SELECT date
FROM car
INNER JOIN accident ON acccident.carid = car.id
WHERE plate_number = '34 BUY 543'

date
12.12.2022
05.05.2022
07.12.2000



SELECT count(*)
FROM car
INNER JOIN accident ON acccident.carid = car.id
WHERE plate_number = '34 BUY 543'

3

2000 AZN 
