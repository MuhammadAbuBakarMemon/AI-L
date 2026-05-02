from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


iris = datasets.load_iris()

x = iris.data 
y = iris.target

x_train, x_test , y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 42)

DT = DecisionTreeClassifier()
ModelDT = DT.fit(x_train, y_train)

PredictionDT = DT.predict(x_test)
print("Prediction: ", PredictionDT)

# Testign Accurcy - accuracy_score() 
# r^2 score - r2_score()
# Mean Squared Accuracy - mean_sqaured_error()  

# ONLY FOR DT
# Training acuracy - score()
# it takes both the training parameters   

print("\nDT Trainig Accuracy: \n")
teaccDT = DT.score(x_train, y_train)
te_per = teaccDT * 100 
print(f"Model Training Accuracy:  {te_per:.2f}\n")

print("\nDT Testing Accurary: \n")
teacDT = accuracy_score(y_test, PredictionDT)
t_per = teacDT * 100
print(f"Testing Accuracy (%): {t_per:.2f}") 




