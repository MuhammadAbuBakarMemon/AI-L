import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets

iris = datasets.load_iris()

x = iris.data
y = iris.target 

# Split the data
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


# Important Insight (Exam-worthy):

# If you see:

# Training Accuracy ≈ 100%
# Testing Accuracy much lower

# Your Decision Tree is likely overfitting

# To fix that, you can control the tree:

# DT = DecisionTreeClassifier(max_depth=3)