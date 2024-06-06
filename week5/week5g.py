import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


f = "week5_diabetes_binary_health_indicators_BRFSS2015.csv"
df = pd.read_csv(f)


# Creating a crosstab to count occurrences
heatmap_data = pd.crosstab(df['Veggies'], df['Fruits'])
print(heatmap_data)



# Plotting heatmap
#plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=False, cmap='vlag')
plt.title('Heatmap of Column1 vs Column2')
plt.show()
