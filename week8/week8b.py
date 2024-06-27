
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split


#: For some algorithms, we need to scale our variables!
#  One of them is "neural networks"
#  All inputs, and output(s) must be scaled between [0, 1] or [-1, 1]
#  Z-score is usually optimal
#  Min-max normalizer
#  


# min...
# 
# 
# 
# avg...
# 
# 
# 
# max...

# (x - x_mean) / x_std


X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)

clf = RandomForestClassifier(.....)
clf.fit()

clf = MLPClassifier(max_iter=300, hidden_layer_sizes = (20, 3))
clf.fit(X_train, y_train)



clf.predict(X_test[:5, :])
