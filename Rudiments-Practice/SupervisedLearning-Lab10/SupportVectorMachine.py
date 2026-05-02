from sklearn import datasets 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#load dataset
iris = datasets.load_iris()

#input values, ke columns loaded - independent variables - predictor variables 
x = iris.data
#target vales / labels - dependent variable - output variable
y = iris.target

#now we have to classify y in a binary form like currectly on the bassi of our data set y represents 3 classes of flowers, we need to transform these 3 
#into 2 classes so binary classification is a possibiloty

y = (y == 0).astype(int)

# CURRENTLY WE HAVE Y LIKE THIS 
# [Setosa, versicolor, Virigina]
# [0,     ,1          , 2     ]
# @these indexes 

# (y == 0) - evaluates to a boolean array setting TRUE where y == 0th index -> Sestoa
# then .astype(int) converts it into a numeric value 

#trick to remember pehle we sit in train then do the testing but x first then y 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

#train svm model with rbf kernel
svm = SVC(kernel='rbf', C=1, gamma='scale')
svm.fit(x_train, y_train)

#making predictions 
y_pred = svm.predict(x_test)

#evaluating the model 
print("Accuracy Score: ", accuracy_score(y_test, y_pred))
