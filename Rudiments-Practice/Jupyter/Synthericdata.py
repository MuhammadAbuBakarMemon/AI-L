import pandas as pd
from sklearn.datasets import make_classification

# ==============================================================================
# APPROACH 1: USING SCIKIT-LEARN GENERATORS
# ==============================================================================
# Scikit-learn provides functions like 'make_classification', 'make_regression', 
# and 'make_blobs' to instantly generate complex, mathematically related data.
# This is ideal when you need a dataset to test a machine learning model.
# ==============================================================================

# make_classification generates a random dataset consisting of feature columns (X)
# and a target label column (y) that is mathematically related to those features.
X, y = make_classification(
    n_samples=100,         # Total number of rows to generate
    n_features=4,          # Total number of feature columns
    n_informative=2,       # How many features actually affect the target label
    n_redundant=1,         # How many features are just random noise/copies
    n_classes=2,           # Binary classification (target is 0 or 1)
    random_state=42        # Sets a seed so you get the exact same data every time
)

# Convert the generated features (X) into a Pandas DataFrame
# We name the columns Feature_1, Feature_2, etc.
df_sklearn = pd.DataFrame(X, columns=['Feature_1', 'Feature_2', 'Feature_3', 'Feature_4'])

# Add the target labels (y) as a new column at the end of the DataFrame
df_sklearn['Target'] = y

# Print the first 5 rows to see the result
print("Scikit-Learn Synthetic Data:")
print(df_sklearn.head())