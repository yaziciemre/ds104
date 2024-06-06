import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


f = "week5_coffee.csv"
df = pd.read_csv(f)

df['transaction_date'] = pd.to_datetime(df['transaction_date'], format = "%d-%m-%Y")
df['Month'] = df['transaction_date'].dt.month
df['WeekDay'] = df['transaction_date'].dt.weekday
df['transaction_time'] = pd.to_datetime( df['transaction_time'], format='%H:%M:%S' )
df['Hour'] = df['transaction_time'].dt.hour


# Creating a crosstab to count occurrences
heatmap_data = pd.crosstab(df['Month'], df['Hour'])
print(heatmap_data)

# Plotting heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=False, cmap='coolwarm')
plt.title('Heatmap of Column1 vs Column2')
plt.show()
