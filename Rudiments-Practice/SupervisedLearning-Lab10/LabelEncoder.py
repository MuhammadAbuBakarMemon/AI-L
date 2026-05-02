# USED FOR OUTPUT DATA  - 1 COLUMN

#how to encode data - converting string into numeric data 

# what happened internally 
# the label encoder found unique labels
# [setosa, versicolor, virginica]

# and assigns them numbers alphabetically

from sklearn import datasets 

from sklearn.preprocessing import LabelEncoder 

iris = datasets.load_iris()

x = iris.data
y = iris.target

le = LabelEncoder()
y_encoded = le.fit_transform(y)

print(y_encoded)

print()

# reverse map out such stuff

print(le.inverse_transform([0, 1, 2]))


# The "Hidden" LabelingIn the iris dataset provided by sklearn, the target variable y is already encoded as 
# integers ($0, 1, 2$).When you run le.fit_transform(y), the LabelEncoder sees the numbers $0, 1, 2$ and maps 
# them to... $0, 1, 2$. It essentially maps the numbers to themselves. Therefore, when you call inverse_transform, it just gives you back the 
# integers it learned.

# To get the flower names, you need to map those integers back to the target names stored within the dataset object. 
# Here is how you can see the actual names:

# The names are stored here:
# iris.target_names -> ['setosa', 'versicolor', 'virginica']
y_names = [iris.target_names[i] for i in iris.target]

le2 = LabelEncoder()
y_en = le2.fit_transform(y_names)

print(y_en)

print(le2.inverse_transform([0,1,2]))