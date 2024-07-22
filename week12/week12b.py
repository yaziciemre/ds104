import h2o
from h2o.automl import H2OAutoML
h2o.init()

# Load a sample dataset from H2O
data = h2o.import_file("w12_train.csv")

# Split the data into training and test sets
train, test = data.split_frame(ratios=[0.8])

# Identify predictors and response
x = train.columns
y = "SalePrice"

# Remove the response column from the predictor set
x.remove(y)

# Initialize and train H2O AutoML
aml = H2OAutoML(max_models=5, seed=1)
aml.train(x=x, y=y, training_frame=train)

# View the AutoML leaderboard
lb = aml.leaderboard
print(lb)

# Get the best model
best_model = aml.leader

# Make predictions on the test set
predictions = best_model.predict(test)
print(predictions)

h2o.shutdown()

