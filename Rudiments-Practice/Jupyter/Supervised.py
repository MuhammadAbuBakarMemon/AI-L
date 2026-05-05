#Linear Regression 

import random

random.seed(42)

print(random.randint(1, 10))
print(random.randint(1, 10))

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate some sample data
# Let's say we are predicting 'y' based on 'x'
np.random.seed(42)

# x will be a 2D array with 100 samples and 1 feature
x = np.random.rand(100, 1) * 10  # Random values between 0 and 10

# y will be a linear function of x with some noise
y = 3 * x.flatten() + np.random.randn(100) * 2  # y = 3 * x + noise

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
LR = LinearRegression()
ModelLR = LR.fit(x_train, y_train)

# Predict on the test data
PredictionLR = ModelLR.predict(x_test)

# Print the predictions
print("Predictions:", PredictionLR)

# Optional: Print the Mean Squared Error (MSE) to evaluate the model
mse = mean_squared_error(y_test, PredictionLR)
print(f"Mean Squared Error: {mse}")


#SVM

from sklearn import datasets
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
y = (y == 0).astype(int)  # Convert to binary classification problem

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train SVM model with RBF kernel
svm = SVC(kernel='rbf', C=1, gamma='scale')
svm.fit(X_train, y_train)

# Make predictions
y_pred = svm.predict(X_test)

# Evaluate the model
print("SVM Accuracy:", accuracy_score(y_test, y_pred))


#DECISION TREE

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

# Example Data (make sure to define x and y)
# Let's generate some simple data for classification
# x will be random values, and y will be a binary classification target
np.random.seed(42)

# x = 100 samples with 5 features each
x = np.random.rand(100, 5)

# y = binary target with values 0 or 1
y = np.random.randint(0, 2, 100)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize the DecisionTreeClassifier
DT = DecisionTreeClassifier()

# Train the model
ModelDT = DT.fit(x_train, y_train)

# Model Testing (Prediction)
PredictionDT = DT.predict(x_test)
print("Predictions:", PredictionDT)

# Model Training Accuracy
print('====================DT Training Accuracy===============')
tracDT = DT.score(x_train, y_train)  # The score method gives accuracy directly
TrainingAccDT = tracDT * 100
print(f"Training Accuracy: {TrainingAccDT:.2f}%")

# Model Testing Accuracy
print('=====================DT Testing Accuracy=================')
teacDT = accuracy_score(y_test, PredictionDT)
testingAccDT = teacDT * 100
print(f"Testing Accuracy: {testingAccDT:.2f}%")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.1, random_state=42)

from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
iris = datasets.load_iris()


iris

iris.feature_names

iris.target_names

df = ['age', 'gender', 'height', 'weight', 'obese']

X = df['age', 'gender', 'height', 'weight']
y = df['obese']

#clustering 

from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score