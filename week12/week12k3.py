from fastapi import FastAPI
import uvicorn
from sklearn.ensemble import RandomForestClassifier
import pickle
import json

file = open('week12_model.pkl', 'rb') # Open a file for [R]EADING, [B]INARY
clf = pickle.load(file)
file.close()

# just like "ANSWER" in a mobile phone, listen!!!
app = FastAPI()

@app.get("/tahmin")
def tahmin( sex,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status ) -> int:
	row = [sex,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]
	return clf.predict( [row] )[ 0 ]


@app.get("/tahmin2")
def tahmin2( data: str ) -> int:
	data = json.loads( data )
	data = list(data.values())
	return clf.predict( [data] )[ 0 ]


if __name__ == "__main__":
    uvicorn.run("week12k3:app", host="127.0.0.1", port=5000, reload=True)
