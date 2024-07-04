

s = "week9_smoke_train_dataset.csv"
import pandas as pd
df = pd.read_csv(s)

import matplotlib.pyplot as plt
import numpy as np
# method: sigmoid
# Sigmoid function
# @x: The input values
# @return: The output values
# @completed
def sigmoid(x, derivative=False):
    return x*(1-x) if derivative else 1/(1+np.exp(-x))

xs = []
ys = []

for i in df['hemoglobin'].unique():
	xs.append(i)
	ys.append( df[ df['hemoglobin'] == i ]['smoking'].mean() )

plt.scatter( xs, ys )


df['hemoglobin2'] = (df['hemoglobin'] - df['hemoglobin'].mean()) / df['hemoglobin'].std()
df['my1'] = df['hemoglobin2'].map(sigmoid)
print( df['my1'].corr( df['smoking'] ) )


plt.show()
