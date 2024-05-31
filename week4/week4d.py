

file = "week4_Invistico_Airline.csv"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#: Load the data in file into a variable called df (dataframe)
df = pd.read_csv(file)


print( df['Flight Distance'] )
print( "max", df['Flight Distance'].max() )
print( "min", df['Flight Distance'].min() )
print( "avg", df['Flight Distance'].mean() )
print( "mode", df['Flight Distance'].mode() )
print( "median", df['Flight Distance'].median() )
print( "std", df['Flight Distance'].std() )
print( "count", len(df['Flight Distance']) )

print( "q1", df['Flight Distance'].quantile(0.25) )



upper = df['Flight Distance'].mean() + df['Flight Distance'].std() * 3
lower = df['Flight Distance'].mean() - df['Flight Distance'].std() * 3



df = df[ df['Flight Distance'] < upper ]
df = df[ df['Flight Distance'] > lower ]


#! FILTERING


plt.hist( df['Flight Distance'] )

plt.show()