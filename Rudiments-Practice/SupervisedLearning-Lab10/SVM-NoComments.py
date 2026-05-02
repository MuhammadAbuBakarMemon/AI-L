from sklearn import datasets 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

x = iris.data
y = iris.target

y = (y == 0).astype(int)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 42)

svm = SVC(kernel='rbf', C=1, gamma='scale')
svm.fit(x_train, y_train)

y_predict = svm.predict(x_test)

print("Accuracy Score: ", accuracy_score(y_predict, y_test))
