import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('Mall_Customers.csv')
df.head()

x = df.iloc[ : , [3, 4]].values

scalar = StandardScaler()
x_scaled = scalar.fit_transform(x)

wcss_list = []

for m in range(1, 11):
    kmeans = KMeans(n_clusters = m, init = 'k-means++', n_init = 10, random_state = 42)
    kmeans.fit(x_scaled)
    wcss_list.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss_list)
plt.title("The Elbow Method Graph")
plt.xlabel("Number of Clusters(k)")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans (n_clusters=5, init='k-means++', n_init=10, random_state = 42)
y_predict = kmeans.fit_predict(x_scaled)

unscaled_centroids = scalar.inverse_transform(kmeans.cluster_centers_)

plt.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s = 100, c = 'blue', label = 'Cluster 1')
plt.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s = 100, c = 'green', label = 'Cluster 2')
plt.scatter(x[y_predict == 2, 0], x[y_predict == 2, 1], s = 100, c = 'red', label = 'Cluster 3')
plt.scatter(x[y_predict == 3, 0], x[y_predict == 3, 1], s = 100, c = 'purple', label = 'Cluster 4')
plt.scatter(x[y_predict == 4, 0], x[y_predict == 4, 1], s = 100, c = 'black', label = 'Cluster 5') 

plt.scatter(unscaled_centroids[: , 0], unscaled_centroids[: , 1], s = 300, c = 'yellow', label = 'Centroids')

plt.title("Clusters of customers")
plt.xlabel("Annual Income k($)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
