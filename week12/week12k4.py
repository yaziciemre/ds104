

import requests
"""
import json
import pandas as pd
df = pd.read_csv("week9_stroke_data.csv")
df = df.dropna()
randomrow = df.iloc[3453].to_dict()
print(json.dumps(randomrow))
"""

sample = """{"sex": 0.0, "age": 62.0, "hypertension": 0.0, "heart_disease": 1.0, "ever_married": 1.0, "work_type": 4.0, "Residence_type": 0.0, "avg_glucose_level": 240.59, "bmi": 31.4, "smoking_status": 1.0}"""

url = "http://localhost:5000/tahmin2?data=" + sample

# just like "CALL" in a mobile phone, TELL
x = requests.get(url)

print(x.text)

