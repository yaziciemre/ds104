
import random
import pandas as pd
f = "week8_patient_dataset.csv"
Target = "hospital_death"

df = pd.read_csv(f)

# - descriptive analysis
# - removing outliers
# - removing unnecessary columns
# - filling nulls
# - feature mining, feature extraction, data enrichment

# - modelling


df = df.dropna()
df = df.select_dtypes(exclude = ['object'])
del df['hospital_id']


df['Year'] = 2014
df['Year'] = df['Year'].apply(lambda value: random.randint(2014,2024))

# Data weighting! (data aging)
# Very important

y2024 = df[ df['Year'] == 2024 ].sample(frac = 0.80)
y2023 = df[ df['Year'] == 2023 ].sample(frac = 0.70)
y2022 = df[ df['Year'] == 2022 ].sample(frac = 0.60)
y2021 = df[ df['Year'] == 2021 ].sample(frac = 0.50)
y2020 = df[ df['Year'] == 2020 ].sample(frac = 0.40)
y2019 = df[ df['Year'] == 2019 ].sample(frac = 0.30)
y2018 = df[ df['Year'] == 2018 ].sample(frac = 0.20)
y2017 = df[ df['Year'] < 2018 ].sample(frac = 0.10)


y2024 = df[ df['Year'] == 2024 ].sample(frac = 1.00)
y2023 = df[ df['Year'] == 2023 ].sample(frac = 0.70)
y2022 = df[ df['Year'] == 2022 ].sample(frac = 0.50)
y2021 = df[ df['Year'] == 2021 ].sample(frac = 0.30)
y2020 = df[ df['Year'] == 2020 ].sample(frac = 0.10)
y2019 = df[ df['Year'] == 2019 ].sample(frac = 0.05)
y2018 = df[ df['Year'] == 2018 ].sample(frac = 0.01)

# We shuffle data, but before that we update their WEIGHTS!, COEFFICIENT, HOW IMPORTANT THEY ARE, IMPORTANCE
#: Data Aging
df = pd.concat([y2024, y2023, y2022, y2021, y2020, y2019, y2018, y2017])
df = df.sample(frac = 1.0)

del df['Year']

#: Assignment ==> Find a dataset which has year or a date, apply data aging!

print(df)




