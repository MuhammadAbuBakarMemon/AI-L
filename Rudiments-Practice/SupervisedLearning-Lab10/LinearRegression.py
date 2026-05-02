import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Example dataset (ONLY if x and y are not already defined)
# Remove this if you already have x and y
from sklearn.datasets import load_iris
data = load_iris()
x = data.data
y = data.target

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
LR = LinearRegression()
ModelLR = LR.fit(x_train, y_train)

# Predict on the test data
PredictionLR = ModelLR.predict(x_test)

# Print the predictions
print("Predictions:", PredictionLR)

# Evaluate the model using Mean Squared Error
mse = mean_squared_error(y_test, PredictionLR)
print("Mean Squared Error:", mse)

# R² Score (Testing Accuracy)
print("===================LR Testing Accuracy================")
teachLR = r2_score(y_test, PredictionLR)
testingAccLR = teachLR * 100
print("R² Accuracy (%):", testingAccLR)

# Optional: Compare actual vs predicted
print("\nActual vs Predicted:")
for actual, predicted in zip(y_test, PredictionLR):
    print(f"Actual: {actual}, Predicted: {predicted:.2f}")