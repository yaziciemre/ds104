
import sys
from sklearn.ensemble import RandomForestClassifier
import os
import pickle
import pandas as pd
import random


file = open('week12_model.pkl', 'rb') # Open a file for [R]EADING, [B]INARY
clf = pickle.load(file)
file.close()

df = pd.read_csv('week9_stroke_data.csv')
randomrow = df.iloc[ random.randint(0, len(df) - 1) ]
#del randomrow['stroke']
#print(randomrow.to_dict())
#print(clf.predict( [randomrow] )[0])

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/tahmin")
def tahmin( sex,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status ) -> int:
	row = [sex,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]
	return clf.predict( [row] )[ 0 ]

#print("Tahmin sonucu", tahmin( 1, 63, 0, 0,1,4,1,220,36,1 ))

"""
randomrow = randomrow.to_dict()
s = "tahmin?"
for c in randomrow:
	s += c + "=" + str(randomrow[c]) + "&"
"""
# query
# http://localhost:5000/tahmin?sex=1.0&age=77.0&hypertension=0.0&heart_disease=0.0&ever_married=1.0&work_type=4.0&Residence_type=1.0&avg_glucose_level=142.31&bmi=29.1&smoking_status=1.0&stroke=0.0


@app.get("/getSum")
def getSum( a, b ):
    return int(a) + int(b)


@app.get("/FahrenheitToCelcius")
def FahrenheitToCelcius( f ):
	f = float(f)
	return (f - 32) / 1.8

@app.get("/bloodPressureLevel")
def bloodPressureLevel( b ):
	b = int(b)
	if b > 110: return 'high'
	if b > 90: return 'abovenormal'
	if b > 70: return 'normal'
	if b > 50: return 'low'
	return 'verylow'


if __name__ == "__main__":
    uvicorn.run("week12k2:app", host="127.0.0.1", port=5000, reload=True)
