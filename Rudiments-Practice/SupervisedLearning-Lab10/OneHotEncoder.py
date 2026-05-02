# USED FOR INPUT DATA - MULTIPLE COLUMNS    

import numpy as np
from sklearn.preprocessing import OneHotEncoder

y = ["setosa", "versicolor", "virginica", "setosa", "virginica"]

# reshape(rows, cols) - -1 indicated figure them out on your own to the interpreter 

# convert yo numpy array 
# shape to 2D

y = np.array(y).reshape(-1, 1)

ohe = OneHotEncoder()

# need to convert toarray() 
# bcs by default fit_transform returns a sparse matrix stores only the non-zero values (to save memory), we convert it into a dense numpy array
y_ohe = ohe.fit_transform(y).toarray()

print("Original Labels: \n", y)
print("OneHotEncoded Labels: \n", y_ohe)

print("\ncategories: ", ohe.categories_)