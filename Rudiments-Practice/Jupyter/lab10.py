# from collections import defaultdict

# class NetworkGraph:
#     def __init__(self):
#         self.nodes = set()
#         self.edges = defaultdict(list)

#     def add_node(self, node):
#         self.nodes.add(node)

#     def add_edge(self, start, end):
#         if start not in self.nodes or end not in self.nodes:
#             raise ValueError("Both nodes must exist in the graph")
#         self.edges[start].append(end)
#         self.edges[end].append(start)  # Assuming the graph is undirected

#     def bfs_search(self, start_node, infected_systems):
#         visited = set()
#         queue = [(start_node, [start_node])]

#         while queue:
#             node, path = queue.pop(0)

#             if node == infected_systems:
#                 return path
#             visited.add(node)
#             for neighbor in self.edges[node]:
#                 if neighbor not in visited and neighbor != start_node:
#                     new_path = list(path)
#                     new_path.append(neighbor)
#                     queue.append((neighbor, new_path))

#         # If no path is found
#         return None

#     def dfs_search(self, start_node, infected_systems):
#         visited = set()
#         stack = [(start_node, [start_node])]

#         while stack:
#             node, path = stack.pop()

#             if node == infected_systems:
#                 return path
#             visited.add(node)
#             for neighbor in self.edges[node]:
#                 if neighbor not in visited:
#                     new_path = list(path)
#                     new_path.append(neighbor)
#                     stack.append((neighbor, new_path))

#         # If no path is found
#         return None

# # Create a network graph
# graph = NetworkGraph()
# nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# edges = [('H', 'A'), ('H', 'C'), ('H', 'G'), ('G', 'C'), ('C', 'D'), ('C', 'B'), ('B', 'F'), ('A', 'F'), ('B', 'E'), ('E', 'I')]
# for start, end in edges:
#     graph.add_node(start)
#     graph.add_node(end)
#     graph.add_edge(start, end)

# infected_systems = 'I'

# # Perform BFS search
# bfs_path = graph.bfs_search('H', infected_systems)
# if bfs_path:
#     print("Shortest path (BFS):", bfs_path)
# else:
#     print("No path found using BFS")

# # Perform DFS search
# dfs_path = graph.dfs_search('H', infected_systems)
# if dfs_path:
#     print("Shortest path (DFS):", dfs_path)
# else:
#     print("No path found using DFS")


import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv('heart.csv')
# x=data['age']
# y=data['sex']
y=data.pop('target')
data

#sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

train_test_split(data,y,test_size=0.2)


lr= LogisticRegression()
lr_model=lr.fit(xtrain , ytain)
prediction = lr_model.predict(xtest)
lr.score(xtest,ytest)

#Sci-kit learn

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)
print("Predictions:", model.predict(X))

# Example of using Scikit-learn to train a classifier (Logistic Regression)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a logistic regression model
model = LogisticRegression(max_iter=200)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')


#seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = pd.DataFrame({'x': [1,2,3,4,5], 'y': [2,4,6,8,10]})

# Create scatter plot
sns.scatterplot(x='x', y='y', data=data)
plt.title("Seaborn Scatter Plot")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Example: Visualizing pairplot of Iris dataset
sns.pairplot(sns.load_dataset("iris"), hue="species")
plt.show()

#NUMPY

import numpy as np

# Example: Create a NumPy array and perform basic operations
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))  # Mean of the array
print(np.sum(arr))

#PANDAS

import pandas as pd

# Example: Loading a CSV file into a DataFrame
df = pd.read_csv('/content/sample_data/california_housing_test.csv')

# Display first 5 rows0
print(df.tail())

#MATPLOTLIB

categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 30]

plt.bar(categories, values, color='green')
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")
plt.show()


import matplotlib.pyplot as plt

# Example: Plotting a simple line graph
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.title('Sample Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


#READING AND WRITING TO CSV FILES 

import pandas as pd
df = pd.read_csv("data.csv")  # Reading a CSV file
df.to_csv("output.csv", index=False)  # Writing to a CSV file
print(df.head())  # Display first few rows


#HANDLING MISSING VALUES 
# Load Titanic dataset
df = sns.load_dataset("titanic")

# Display first 5 rows
df.head()

# Check for missing values
print(df.isnull().sum())
# Drop missing values
df_cleaned = df.dropna()
print("Dataset after dropping missing values:", df_cleaned.shape)
# Handle missing values
df['age'] = df['age'].fillna(df['age'].mean())  # Fill age with mean
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])  # Fill embarked with mode

# Convert deck to string and replace NaN
df['deck'] = df['deck'].astype(str).fillna('Unknown')

# Drop remaining NaN values if needed
df = df.dropna()

print(df.isnull().sum())  # Confirm no missing values


#ENCODING CATEGORICAL VALUES 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder

le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])  # 0 for male, 1 for female
print(df['sex'].head())

#Creates separate binary columns for each category.
df = pd.get_dummies(df, columns=['embarked'], drop_first=True)
print(df.head())

#DATA VISUALISATION

df[['age', 'fare']].hist(bins=20, figsize=(8,4))
plt.show()


#TRAINTESTSPLIT USING NAIVE BAYES
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np

# Generate dummy dataset
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = np.random.randint(0, 2, 100)  # Binary target variable (0 or 1)

# Splitting the data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Naïve Bayes model
model = GaussianNB()

# Train the model on training data
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")


#KFOLDS CROSS VALIDATIONN

from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import seaborn as sns

# Load dataset
df = sns.load_dataset("titanic")

# Select features and target, handling missing values
X = df[['age', 'fare']].fillna(df[['age', 'fare']].mean())
y = df['survived']

# Convert to DataFrame to use .iloc[]
X = pd.DataFrame(X)
y = pd.Series(y)

# Define K-Fold (5 splits)
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Initialize model
model = LogisticRegression()

# Store accuracy scores
accuracy_scores = []

# Perform K-Fold CV
for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]  # Now X is a DataFrame
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]  # Now y is a Series

    # Train model
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy_scores.append(acc)

# Print average accuracy
print("K-Fold CV Average Accuracy:", np.mean(accuracy_scores))


#LOOCV

from sklearn.model_selection import LeaveOneOut

# Initialize LOOCV
loo = LeaveOneOut()

# Store accuracy scores
loo_scores = []

# Perform LOOCV
for train_index, test_index in loo.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    # Train model
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    loo_scores.append(accuracy_score(y_test, y_pred))

# Print average accuracy
print("LOOCV Average Accuracy:", np.mean(loo_scores))

#ROC CURVE 

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Assuming the model has been trained and 'PredictionDT' holds class predictions
# To compute ROC, we need the probability estimates, not just the predicted class.
# For binary classification, use the probabilities of the positive class.

# Get probabilities for the positive class
probabilities = DT.predict_proba(x_test)[:, 1]  # Get the probability for class '1'

# Calculate ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, probabilities)

# Calculate ROC_AUC Score
roc_auc = roc_auc_score(y_test, probabilities)

# Plot ROC curve with shaded area under the curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.fill_between(fpr, tpr, color='skyblue', alpha=0.4)
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve with AUC Area')
plt.legend(loc='lower right')
plt.show()


