
# Python
import warnings
import matplotlib.pyplot as plt
import pandas as pd
from prophet import Prophet

s = "week11_file_out.csv"
df = pd.read_csv(s)

df = df.groupby('Date').size().reset_index()
df.columns = ['ds', 'y']
df.to_csv("week12_sample.csv", index = False)

# Python
df = pd.read_csv('week12_sample.csv')
print(df.head())

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
print(future.tail())

forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

with warnings.catch_warnings():
	warnings.simplefilter("ignore", FutureWarning)
    # your plotly code
	fig1 = m.plot(forecast)
	fig2 = m.plot_components(forecast)

plt.show()
