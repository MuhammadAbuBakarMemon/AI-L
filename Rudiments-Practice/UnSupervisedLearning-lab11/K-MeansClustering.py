# Importing libraries using standard community aliases
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Importing the dataset 
df = pd.read_csv('Mall_Customers.csv')
df.head()

# Extracting Variables
x = df.iloc[:, [3, 4]].values 

# 1. Normalize features FIRST so both the elbow method and final model use the same data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(x)

# Finding optimal number of clusters using the elbow method 
wcss_list = [] # Initializing the list for the values of WCSS 

# Using for loop for iterations from 1 to 10. 
for i in range(1, 11): 
    # Added n_init='auto' or 10 to suppress FutureWarnings in newer scikit-learn versions
    kmeans = KMeans(n_clusters=i, init='k-means++', n_init=10, random_state=42) #here randon_state controls the initial placement of cluster centroids 
    kmeans.fit(X_scaled) # Fitting on the SCALED data
    wcss_list.append(kmeans.inertia_) #kmeans.inertia_ -> the neatness score 

plt.plot(range(1, 11), wcss_list) 
plt.title('The Elbow Method Graph') # Fixed typo: 'Elobw'
plt.xlabel('Number of clusters(k)') 
plt.ylabel('WCSS')
plt.show() 

# Training the K-means model on the scaled dataset 
kmeans = KMeans(n_clusters=5, init='k-means++', n_init=10, random_state=42) 
y_predict = kmeans.fit_predict(X_scaled) 

# 2. Inverse transform the centroids so they match the unscaled data in the plot
centroids_unscaled = scaler.inverse_transform(kmeans.cluster_centers_)

# Visualizing the clusters (Plotting unscaled 'x' so axis labels make sense: 1-100k)
plt.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s = 100, c = 'blue', label = 'Cluster 1') 
plt.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s = 100, c = 'green', label = 'Cluster 2') 
plt.scatter(x[y_predict == 2, 0], x[y_predict == 2, 1], s = 100, c = 'red', label = 'Cluster 3') 
plt.scatter(x[y_predict == 3, 0], x[y_predict == 3, 1], s = 100, c = 'black', label = 'Cluster 4') 
plt.scatter(x[y_predict == 4, 0], x[y_predict == 4, 1], s = 100, c = 'purple', label = 'Cluster 5') 

# Plotting the inverse-transformed centroids
plt.scatter(centroids_unscaled[:, 0], centroids_unscaled[:, 1], s = 300, c = 'yellow', label = 'Centroid') 

plt.title('Clusters of customers') 
plt.xlabel('Annual Income (k$)') 
plt.ylabel('Spending Score (1-100)') 
plt.legend() 
plt.show()

