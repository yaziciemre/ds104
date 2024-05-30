import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as st

def getInformation( mylist: np.array ) -> dict:
	stats = {}

	stats[ 'mean' ] = round(np.mean(mylist), 3)
	stats[ 'std' ] = round( np.std(mylist), 3)
	stats[ 'dev' ] = round( stats['std'] / stats['mean'], 3)
	stats[ 'max' ] = np.max( mylist )
	stats[ 'min' ] = np.min( mylist )
	stats[ 'count' ] = len( mylist )
	stats[ 'range' ] = stats['max'] - stats['min']
	stats[ 'mean+std' ] = round(stats['mean'] + stats['std'], 3)
	stats[ 'mean-std' ] = round(stats['mean'] - stats['std'], 3)
	stats[ '#inrange1' ] = len( mylist[ (mylist > stats['mean-std']) & (mylist < stats['mean+std']) ] )
	stats[ '%inrange1' ] = round(stats[ '#inrange1' ] / stats['count'], 3)
	stats[ 'upper1' ] = stats['mean'] + 3 * stats['std']
	stats[ 'lower1' ] = stats['mean'] - 3 * stats['std']
	stats[ 'q1' ] = np.quantile(mylist, 0.25)
	stats[ 'q2' ] = np.quantile(mylist, 0.50) # median, medyan
	stats[ 'q3' ] = np.quantile(mylist, 0.75)
	stats[ 'iqr' ] = stats['q3'] - stats['q1']
	stats[ 'upper2' ] = stats['q3'] + 1.5 * stats['iqr']
	stats[ 'lower2' ] = stats['q1'] - 1.5 * stats['iqr']
	stats[ 'mode' ] = st.mode(mylist)
	stats[ 'skew' ] = st.skew(mylist)
	stats[ 'kurt' ] = st.kurtosis(mylist) # kurtosis

	return stats

numbers = [60, 60, 60, 65, 65, 65, 66, 67, 55, 21, 62, 53, 54, 46, 154, 151, 33, 63, 53, 47, 36, 37, 46, 48, 58, 55, 40, 52, 63, 45, 37, 53, 47, 35, 63, 42, 62, 67, 42, 68, 48, 57, 43, 60, 57, 47, 66, 46, 31, 49, 48, 56, 38, 49, 29, 60, 43]
import collections
counter = collections.Counter(numbers)
print(counter)
# Counter({42: 5, 60: 3, 53: 3, 46: 3, 47: 3, 48: 3, 55: 2, 37: 2, 63: 2, 57: 2, 43: 2, 49: 2, 21: 1, 54: 1, 154: 1, 151: 1, 33: 1, 36: 1, 58: 1, 40: 1, 52: 1, 45: 1, 35: 1, 62: 1, 67: 1, 68: 1, 31: 1, 56: 1, 38: 1, 29: 1})







numbers = np.array(numbers)

percentile = [
	np.percentile( numbers, 20 ),
	np.percentile( numbers, 40 ),
	np.percentile( numbers, 60 ),
	np.percentile( numbers, 80 ),
]

percentile = [
	np.percentile( numbers, 15 ),
	np.percentile( numbers, 30 ),
	np.percentile( numbers, 45 ),
	np.percentile( numbers, 60 ),
	np.percentile( numbers, 75 ),
	np.percentile( numbers, 90 ),
]


# [42.2, 48.0, 56.6, 63.0]
# 0-42, 42-48, 48-56, 56-63, 63+
# 100 , 100  , 100  ,  100 , 100



print(percentile)


info = getInformation( numbers )
print(info)
"""
'max': 68,
'min': 21, 
'range': 47, 

'mean': 48.32,
'std': 10.104,
'dev': 0.209, 

'count': 50, 

'mean+std': 58.424, 
'mean-std': 38.216, 
'#inrange1': 32, 
'%inrange1': 0.64
"""


# =====================
# quartile : 1/4 (ceyrek) 0.25
# Suppose we have a data of 500 items
# Divide into 4
# 125


# =====================





# 42.0 48.0 57.0


# OUTLIER / EXTREME VALUE
# mean + 3 * std ==> outlier : Aykiri gozlem, kapsam disi
# Assumption 1 [statistical range to identify outliers]

#: Eliminate the outliers
#numbers = numbers[ numbers < info['upper1'] ]
#numbers = numbers[ numbers > info['lower1'] ]


# Assumption 2 [IQR] Inter quartile range
# International ==> between the nations
# national ==> with in the nation

q25 = np.quantile(numbers, 0.25) # q1
q50 = np.quantile(numbers, 0.50) # q2
q75 = np.quantile(numbers, 0.75) # q3

iqr = q75 - q25
upper = 1.5 * iqr + q75
lower = q25 - 1.5 * iqr

print(q25, q50, q75, upper, lower)

print( "LEFT", len(numbers[ numbers <= q50 ]))
print( "RIGHT", len(numbers[ numbers >= q50 ]))

# MEAN is the average of the values
# MEDIAN is the center point (left side = right side BY COUNT!!!)
# MODE: most frequent item, which item has been used MOST

# print("MODE", stats.mode(numbers))



# filter outliers
numbers = numbers[ numbers < upper ]
numbers = numbers[ numbers > lower ]

plt.hist( numbers )
plt.axvline(q25, color='k', linestyle='dashed', linewidth=1)
plt.axvline(q50, color='k', linestyle='dashed', linewidth=1)
plt.axvline(q75, color='k', linestyle='dashed', linewidth=1)


plt.show()



# Ages ==> 56,45,34,23.....
# Range !!

# 25-30, 30-35, 35-40, 40-50, 50-60.....
# survey, anket, poll

# maks:100, min:20
# range = 80
# 80 / 8  == 10
