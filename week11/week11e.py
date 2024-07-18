import sys
import matplotlib.pyplot as plt
import pandas as pd
s = "week11_sales_06_FY2020-21.csv"
s = "week11_file_out.csv"
df = pd.read_csv(s)

#1. method
#d = df['Date'].value_counts().to_dict()
#df = pd.DataFrame(columns = ['date', 'sales'], data = d.items())

#2. method
df = df.groupby('Date').size().reset_index()
df.columns = ['date', 'sales']
df = df[-365:]

def linreg(X, Y):
    """
    return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
    """
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det


x = list(df['sales'].values)
m, n = linreg(range(len(x)),x) 

#0.09144989302186697 9.873927689198293
#y = 0.091 * x + 9.87
#y = m.x + n
# neft_miktari = 0.454 * gaz_pedal + constant_neft_harcama

df['index'] = [i+1 for i in range(len(df))]
df['trend'] = df['index'] * m + n
df['trend'] = df['trend'].astype(int)

df['de-trend'] = df['sales'] - df['trend']

# How many days later
HOW_MANY_DAYS_LATER = 3
# ADV: if we increase this value, we will be able to forecast FAR MORE FUTURE
# DIS: but it will become more difficult because the correlation will be lower

HOW_MANY_DAYS_BEFORE_TO_LOOK_FOR = 7
# ADV: if we increase this value, we will have MORE features!!
# DIS: less data [dropna]

for i in range(HOW_MANY_DAYS_LATER, HOW_MANY_DAYS_BEFORE_TO_LOOK_FOR + 1): 
	df[f'T-{i}'] = df['sales'].shift(i)
	print(i, df[f'T-{i}'].corr(df['sales']))

df = df.dropna()


df['MA3'] = df['sales'].rolling(3).mean()
df['MA5'] = df['sales'].rolling(5).mean()

df = df.dropna()
df['date'] = pd.to_datetime(df['date'])
df['Year'] = df['date'].dt.year
df['Month'] = df['date'].dt.month
df['Day'] = df['date'].dt.day
df['Weekday'] = df['date'].dt.weekday
df['Weekend'] = df['Weekday'].isin([5,6]).astype(int)

df['Firstdays'] = (df['Day'] < 7).astype(int)
df['Lastdays'] = (df['Day'] > 23).astype(int)

# ice-cream sales
# WINTER == monday, sunday, tuesday ==> low
# SUMMER == tuesday, saturday == > HIGH

month = df.groupby('Month')['sales'].mean().to_dict()
weekday = df.groupby('Weekday')['sales'].mean().to_dict()

df['Month'] = df['Month'].map( month )
df['Weekday'] = df['Weekday'].map( weekday )

print(month)

for c in df.select_dtypes(exclude = ['object', 'datetime']):
	print(c, df[c].corr(df['sales']) )


df.to_csv("week11_TS_sales.csv")

# MODIFICATION OF TARGET
# MAKES OUR PROBLEM EASIER
# df['sales'] = df['sales']
# df['sales'] = df['sales'] - df['sales'].mean()
# df['sales'] = df['sales'] - df['trend']
# df['sales'] = df['sales'] - df['sales'].shift(1) 

plt.plot( df['sales'] )
# plt.show()

# In time series
# 1- There are peaks
#	- indirim
#   - muhtesem friday, campaign
#   - problem mobile application --> call center
#   - president incoming

#   - tatil / holiday
#   - not working
#   - qiymetler kalkmis
#   - website bozuk
# 2- Extreme changes, PERIOD
#   - covid
#   - regulation
#   - crisis
#   - competitors
#   - financial crisis
# 3- Repeating pattern
#   - weekly
#   - monthly
#   - 15 (days)
#   - 90 (days)
#   - 6 (hours)
#   - 12 (hours)
#   - 24 (hours)
#   - 12 (month)
# 4- Average value
# 5- Fluctuation -> std -> ups/downs
#   - small factors!
# 6- Trend
#   - INCREASING, DECREASING
#   - sales increase
#   - incrementing the number of customers
#   - incrementing the number of products


# NO SHUFFLE!!! (cannot shuffle)
# NO MISSING!!! (no missing date)
# NO REPEATING!!! (no duplications)

# DATA AGING
# COK KOHNE --> NOT VERY IMPORNTANT
# COK YENI  --> VERY IMPORTANT

# PERIOD == MONTHLY, 5 years x 12 = 60 
# PERIOD == WEEKLY,  5 years x 52 = 260
# PERIOD == DAILY,   5 years x 365 = 1800
# PERIOD == HALF DAY
# PERIOD == TERM    [morning, noon, evening, night]
# PERIOD == HOUR     5 years x 365 x 24 = 40000

# IN DATA AGING, WE CANNOT SAMPLE
# WE CAN ONLY ASSUME TO TAKE LAST 3 YEARS for example











## SEALED ##

#: Imports
import pandas as pd
from astral.sun import sun
from astral import LocationInfo
#import datetime
#from datetime import datetime as dtime
from datetime import timedelta
import datetime
from calendar import monthrange
from math import ceil
import calendar
import numpy as np
import json
import requests
from GKPConfig import INSERTION
from GKPUtil import *
from statistics import mean
import re






#: The functions which require date only
LAMBDA_day = lambda date_time_obj: date_time_obj.day
LAMBDA_month = lambda date_time_obj: date_time_obj.month
LAMBDA_year = lambda date_time_obj: date_time_obj.year
LAMBDA_population = lambda date_time_obj: DateEnricher.POPULATION[date_time_obj.year]	
LAMBDA_weekend = lambda date_time_obj: int(1 if date_time_obj.weekday() in [5,6] else 0)
LAMBDA_weekday = lambda date_time_obj: int(date_time_obj.weekday())
LAMBDA_season1 = lambda date_time_obj: int(DateEnricher.mapper( 'season1', date_time_obj.month))
LAMBDA_season2 = lambda date_time_obj: int(DateEnricher.mapper( 'season2', date_time_obj.month))
LAMBDA_summerwinter = lambda date_time_obj: int(DateEnricher.mapper( 'summerwinter', date_time_obj.month))
LAMBDA_daysInMonth = lambda date_time_obj: int(monthrange( date_time_obj.year, date_time_obj.month )[1])
LAMBDA_weekOfMonth = lambda date_time_obj: int(DateEnricher.weekOfMonth( date_time_obj ))
LAMBDA_weekOfYear = lambda date_time_obj: int(date_time_obj.isocalendar()[1])
LAMBDA_lastFriday = lambda date_time_obj: int(1 if DateEnricher.lastFriday( date_time_obj.year, date_time_obj.month ) == date_time_obj.day else 0)
LAMBDA_firstMonday = lambda date_time_obj: int(1 if DateEnricher.firstMonday( date_time_obj.year, date_time_obj.month ) == date_time_obj.day else 0)
LAMBDA_lastDays = lambda date_time_obj: int(1 if date_time_obj.day >= 25 else 0)
LAMBDA_firstDays = lambda date_time_obj: int(1 if date_time_obj.day <= 5 else 0)
LAMBDA_monthPercentage = lambda date_time_obj: float(float(date_time_obj.month) / 12.0)
LAMBDA_weeksInMonth = lambda date_time_obj: len(calendar.monthcalendar(date_time_obj.year, date_time_obj.month))
LAMBDA_dayOfYear = lambda date_time_obj: float(date_time_obj.timetuple().tm_yday) / 366.0
LAMBDA_summerBreak = lambda date_time_obj: int(1 if date_time_obj.month in [5,6,7,8] else 0)
LAMBDA_possibleMidTermBreak = lambda date_time_obj: DateEnricher.midTerm( date_time_obj )
LAMBDA_middle = lambda date_time_obj: int(1 if date_time_obj.day in [14, 15, 16] else 0)
#: The functions which require the row
ROW_dayPercentage = lambda date_time_obj, row: float(row['@day']) / float(row['@daysInMonth'])
ROW_weekPercentage = lambda date_time_obj, row: float( row['@weekOfMonth'] ) / float(row['@weeksInMonth'])
ROW_dayLength = lambda date_time_obj, row: DateEnricher.daylength( int(row['@dayOfYear'] * 366.0) ) / 12.0
ROW_lastDayFriday = lambda date_time_obj, row: 1 if row['@weekday'] == 4 and row['@day'] == row['@daysInMonth'] else 0

ROW_dayLengthg10 = lambda date_time_obj, row: int(1 if (row['@dayLength'] * 12.0 ) > 10.0 else 0)
ROW_dayLengthg11 = lambda date_time_obj, row: int(1 if (row['@dayLength'] * 12.0 ) > 11.0 else 0)
ROW_dayLengthg13 = lambda date_time_obj, row: int(1 if (row['@dayLength'] * 12.0 ) > 13.0 else 0)
ROW_dayLengthg14 = lambda date_time_obj, row: int(1 if (row['@dayLength'] * 12.0 ) > 14.0 else 0)

#: Possible dates
def midTerm( date_time_obj: datetime ):
	if date_time_obj.month == 1 and date_time_obj.day > 21: return 1
	if date_time_obj.month == 2 and date_time_obj.day < 21: return 1
	return 0

def best_fit_slope(xs,ys):
	m = (((mean(xs)*mean(ys)) - mean(xs*ys)) / ((mean(xs)**2) - mean(xs*xs)))
	return m

#: Generic
LAMBDA_hour = lambda date_time_obj: date_time_obj.hour
LAMBDA_midnighttime = lambda date_time_obj: int(1 if date_time_obj.hour in [0,1,2,3,4,5,6] else 0)
LAMBDA_morningtime = lambda date_time_obj: int(1 if date_time_obj.hour in [7,8,9,10] else 0)
LAMBDA_noontime = lambda date_time_obj: int(1 if date_time_obj.hour in [11,12,13] else 0)
LAMBDA_afternoontime = lambda date_time_obj: int(1 if date_time_obj.hour in [14,15,16,17] else 0)
LAMBDA_eveningtime = lambda date_time_obj: int(1 if date_time_obj.hour in [18,19,20] else 0)
LAMBDA_nighttime = lambda date_time_obj: int(1 if date_time_obj.hour in [21,22,23] else 0)
LAMBDA_lunchtime = lambda date_time_obj: int(1 if date_time_obj.hour in [12,13,14] else 0)
LAMBDA_worktime1 = lambda date_time_obj: int(1 if date_time_obj.hour in [8,9,10,11,12,13,14,15,16,17] else 0)
LAMBDA_worktime2 = lambda date_time_obj: int(1 if date_time_obj.hour in [8,9,10,11,12,13,14,15,16] else 0)
LAMBDA_worktime3 = lambda date_time_obj: int(1 if date_time_obj.hour in [9,10,11,12,13,14,15,16,17] else 0)
LAMBDA_worktime4 = lambda date_time_obj: int(1 if date_time_obj.hour in [9,10,11,12,13,14,15,16] else 0)
LAMBDA_afterwork = lambda date_time_obj: int(1 if date_time_obj.hour in [18,19,20,21,22,23,0] else 0)
LAMBDA_justafterwork = lambda date_time_obj: int(1 if date_time_obj.hour in [18,19] else 0)
#: Points
LAMBDA_tsunrise = lambda date_time_obj: timeStampToFloat( sun(ISTANBULCITY.observer, date=date_time_obj.date())['sunrise'] )
LAMBDA_tnoon = lambda date_time_obj: timeStampToFloat( sun(ISTANBULCITY.observer, date=date_time_obj.date())['noon'] )
LAMBDA_tsunset = lambda date_time_obj: timeStampToFloat( sun(ISTANBULCITY.observer, date=date_time_obj.date())['sunset'] )
#: Around
ROW_asunrise = lambda date_time_obj, row: int(1 if abs( float(date_time_obj.hour) - row['tsunrise'] ) < 1.5 else 0)
ROW_anoon = lambda date_time_obj, row: int(1 if abs( float(date_time_obj.hour) - row['tnoon'] ) < 1.5 else 0)
ROW_asunset = lambda date_time_obj, row: int(1 if abs( float(date_time_obj.hour) - row['tsunset'] ) < 1.5 else 0)
#: Between
ROW_brisenoon = lambda date_time_obj, row: int(1 if float(date_time_obj.hour) > row['tsunrise'] and float(date_time_obj.hour) < row['tnoon'] else 0)
ROW_briseset = lambda date_time_obj, row: int(1 if float(date_time_obj.hour) > row['tsunrise'] and float(date_time_obj.hour) < row['tset'] else 0)
ROW_bnoonset = lambda date_time_obj, row: int(1 if float(date_time_obj.hour) > row['tnoon'] and float(date_time_obj.hour) < row['tset'] else 0)

#: Calendar day data types
HOUR_DATA_TYPES = json.load(open('collections/hour_data_types.json', 'r'))
