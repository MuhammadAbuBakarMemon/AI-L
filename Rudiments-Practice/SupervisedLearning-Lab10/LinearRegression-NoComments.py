from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.metrics import r2_score 

iris = datasets.load_iris()

x = iris.data
y = iris.target 

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

LR = LinearRegression()
ModelLR = LR.fit(x_train, y_train)

PredictionLR = LR.predict(x_test)

print("PredictionsLR : ", PredictionLR)

mse = mean_squared_error(y_test, PredictionLR)
print("The Mean Squared Error is: ", mse)

print("How well the regression fits\n")
teacLR = r2_score(y_test, PredictionLR)
fitting_per = teacLR * 100 
print(f"R^2 Accuracy Percentage: {fitting_per:.2f}")

#optimal comparison 
print("\nActual vs Predicted: ")
for actual, predicted in zip(y_test, PredictionLR):
    print(f"Actaual: {actual}, Predicted: {predicted:.2f}")


