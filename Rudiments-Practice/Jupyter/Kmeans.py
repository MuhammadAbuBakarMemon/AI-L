import random 

values = {0,}
# values.add(1)
# values.add(2)
values.remove(0)

for i in range(3):
    values.add(random.randint(1,20))

for i in range(3):
    values.add(random.randint(40,60))

for i in range(3):
    values.add(random.randint(80,100))

data = list(values)
data.sort()
print(data)

c1 = random.choice(list(values))
c2 = random.choice(list(values))
c3 = random.choice(list(values))

print(f"""c1 = {c1}, "c2 = {c2}, c3 = {c3}""")

data_seg = {}
# data_seg[data[0]] = []
# print(data_seg)

for i in data:
  data_seg[i] = []
  data_seg[i].append(abs(c1-i))
  data_seg[i].append(abs(c2-i))
  data_seg[i].append(abs(c3-i))

print(data_seg)

set1, set2, set3 = [], [], []

for i in data_seg:
  index = data_seg[i].index(min(data_seg[i]))

  if index == 0:
    set1.append(i)
  elif index == 1:
    set2.append(i)
  else:
    set3.append(i)

print(set1, set2, set3)

c2 = int(sum(set2)/len(set2))
c1 = int(sum(set1)/len(set1))

print(f"""c1 = {c1}, "c2 = {c2}, c3 = {c3}""")

data_seg = {}
# data_seg[data[0]] = []
# print(data_seg)

for i in data:
  data_seg[i] = []
  data_seg[i].append(abs(c1-i))
  data_seg[i].append(abs(c2-i))
  data_seg[i].append(abs(c3-i))

print(data_seg)

set1, set2, set3 = [], [], []

for i in data_seg:
  index = data_seg[i].index(min(data_seg[i]))

  if index == 0:
    set1.append(i)
  elif index == 1:
    set2.append(i)
  else:
    set3.append(i)

print(set1, set2, set3)

c1 = int(sum(set1)/len(set1))
c2 = int(sum(set2)/len(set2))
c3 = int(sum(set3)/len(set3))

print(f"""c1 = {c1}, "c2 = {c2}, c3 = {c3}""")

data_seg = {}
# data_seg[data[0]] = []
# print(data_seg)

for i in data:
  data_seg[i] = []
  data_seg[i].append(abs(c1-i))
  data_seg[i].append(abs(c2-i))
  data_seg[i].append(abs(c3-i))

print(data_seg)

set1, set2, set3 = [], [], []

for i in data_seg:
  index = data_seg[i].index(min(data_seg[i]))

  if index == 0:
    set1.append(i)
  elif index == 1:
    set2.append(i)
  else:
    set3.append(i)

print(set1, set2, set3)

import matplotlib.pyplot as plt
plt.scatter(data, [0,0,0,0,0,0,0,0], c='red')
plt.show()


#kmeans

import kagglehub

# Download latest version
path = kagglehub.dataset_download("shwetabh123/mall-customers")

print("Path to dataset files:", path)

import os

print(os.listdir(path))

print(path+"/Mall_Customers.csv")

import pandas as pd

df = pd.read_csv(path+"/Mall_Customers.csv")
df.head()

x3 = df.iloc[:, [2,3, 4]].values

print(x3.shape)

x3[:5,:]

x = df.iloc[:, [3, 4]].values

x

import matplotlib.pyplot as mtp


#finding optimal number of clusters using the elbow method
from sklearn.cluster import KMeans
wcss_list= [] #Initializing the list for the values of WCSS
#Using for loop for iterations from 1 to 10.
for i in range(1, 11):
  kmeans = KMeans(n_clusters=i, random_state= 42)
  kmeans.fit(x)
  wcss_list.append(kmeans.inertia_)
mtp.plot(range(1, 11), wcss_list)
mtp.title('The Elobw Method Graph')
mtp.xlabel('Number of clusters(k)')
mtp.ylabel('wcss_list')
mtp.show()

# train k mean for 3 clusters

kmeans = KMeans(n_clusters=3, random_state= 12)
kmeans.fit(x)



import matplotlib.pyplot as plt

y_pred = kmeans.predict(x)

plt.scatter(x[:,0], x[:,1], c=y_pred, cmap='viridis')

plt.xlabel("First Column")
plt.ylabel("Second Column")
plt.title("KMeans Clusters")

plt.show()

#complete code 

import matplotlib.pyplot as plt

kmeans = KMeans(n_clusters=2, random_state= 12)
kmeans.fit(x)

y_pred = kmeans.predict(x)

plt.scatter(x[:,0], x[:,1], c=y_pred, cmap='viridis')

plt.xlabel("First Column")
plt.ylabel("Second Column")
plt.title("KMeans Clusters")

plt.show()

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Train model
kmeans = KMeans(n_clusters=3, random_state= 50)
kmeans.fit(x)

# Predict clusters
y_pred = kmeans.predict(x)

# Plot data points
plt.scatter(x[:,0], x[:,1], c=y_pred, cmap='viridis', s=50)

# Plot centroids
plt.scatter(
    kmeans.cluster_centers_[:,0],   # centroid x-values
    kmeans.cluster_centers_[:,1],   # centroid y-values
    s=100,                          # size
    c='red',                        # centroid color
    marker='o',                     # marker style
    edgecolors='black',
    label='Centroids'
)

# Labels and title
plt.xlabel("First Column")
plt.ylabel("Second Column")
plt.title("KMeans Clusters with Centroids")
plt.legend()

plt.show()

# testing on test_data
import numpy as np
import random

test_data = np.array([
    [random.randint(0,140), random.randint(0,100)]
    for i in range(200)
])


# Predict clusters
y_pred = kmeans.predict(test_data)

# Plot data points
plt.scatter(test_data[:,0], test_data[:,1], c=y_pred, cmap='viridis', s=50)

# Plot centroids
plt.scatter(
    kmeans.cluster_centers_[:,0],   # centroid x-values
    kmeans.cluster_centers_[:,1],   # centroid y-values
    s=100,                          # size
    c='red',                        # centroid color
    marker='o',                     # marker style
    edgecolors='black',
    label='Centroids'
)

# Labels and title
plt.xlabel("First Column")
plt.ylabel("Second Column")
plt.title("KMeans Clusters with Centroids")
plt.legend()

plt.show()

#3 features

import matplotlib.pyplot as mtp


#finding optimal number of clusters using the elbow method
from sklearn.cluster import KMeans
wcss_list= [] #Initializing the list for the values of WCSS
#Using for loop for iterations from 1 to 10.
for i in range(1, 11):
  kmeans = KMeans(n_clusters=i, random_state= 42)
  kmeans.fit(x3)
  wcss_list.append(kmeans.inertia_)
mtp.plot(range(1, 11), wcss_list)
mtp.title('The Elobw Method Graph')
mtp.xlabel('Number of clusters(k)')
mtp.ylabel('wcss_list')
mtp.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# Train model
kmeans = KMeans(n_clusters=4, random_state=12)
kmeans.fit(x3)

# Predict clusters
y_pred = kmeans.predict(x3)

# Create 3D figure
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# Plot data points
ax.scatter(
    x3[:,0],          # X-axis
    x3[:,1],          # Y-axis
    x3[:,2],          # Z-axis
    c=y_pred,
    cmap='viridis',
    s=50
)

# Plot centroids
ax.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    kmeans.cluster_centers_[:,2],
    s=200,
    c='red',
    marker='X',
    edgecolors='black',
    label='Centroids'
)

# Labels and title
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_zlabel("Feature 3")
ax.set_title("3D KMeans Clusters with Centroids")
ax.legend()

plt.show()



df['Genre'].unique()

# df["Genre"] = df["Genre"].astype("category").cat.codes # auto encodes alphabetically F -> 0, M -> 1

df["Genre"] = df["Genre"].map({
    "Male": 0,
    "Female": 1
})

df.head()

df['Genre'].unique()

df = df.drop("CustomerID", axis=1)

df.head()

df.shape

# matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, alpha=None, edgecolors=None, label=None)
# Parameter                  Description                                        Allowed Values / Examples

# x, y                       Sequences of data points to plot                   list, array, pands series e.g., [1,2,3], np.array([1,2,3]), df['col]

# s                          Marker size (scalar or array-like)                 int, float or array-like e.g., 50, 100, [20, 40, 60]

# c                          Marker color                                       color name, hex, RGB, or array of values e.g., 'blue', 'red', '#FF5733', (1,0,0), [10, 20, 30]

# marker                     Shape of the marker                                string symbols e.g., 'o' (circle), 's' (square), '^' (traingle), 'x', '+', '*', '.', ','

# cmap                       Colormap for mapping numeric values to colors      predefined colormaps e.g., 'viridis', 'plasma', 'cool', 'hot', 'jet'

# alpha                      Transparency (0 = transparent, 1 = opaque)         float between 0 and 1 e.g., 0.1 (very transparent) , 0.5, 1.0 (fully visible)

# edgecolors                 Color of marker edges                              color values (same formats as c) e.g., 'black', 'none', '#000000'

# label                      Legend label for the dataset                       string e.g., 'Cluster 1', 'Data Points'

import matplotlib.pyplot as plt
import numpy as np

x = np.array([12, 45, 7, 32, 89, 54, 23, 67, 14, 91])
y = np.array([99, 31, 72, 56, 19, 88, 43, 61, 35, 77])

plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

x1 = np.array([160, 165, 170, 175, 180, 185, 190, 195, 200, 205])
y1 = np.array([55, 58, 60, 62, 64, 66, 68, 70, 72, 74])

x2 = np.array([150, 155, 160, 165, 170, 175, 180, 195, 200, 205])
y2 = np.array([50, 52, 54, 56, 58, 64, 66, 68, 70, 72])

plt.scatter(x1, y1, color='blue', label='Group 1')
plt.scatter(x2, y2, color='red', label='Group 2')

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Comparison of Height vs Weight between two groups')
plt.legend()
plt.show()

x = np.array([3, 12, 9, 20, 5, 18, 22, 11, 27, 16])
y = np.array([95, 55, 63, 77, 89, 50, 41, 70, 58, 83])

a = [20, 50, 100, 200, 500, 1000, 60, 90, 150, 300] # size
b = ['red', 'green', 'blue', 'purple', 'orange', 'black', 'pink', 'brown', 'yellow', 'cyan'] # color

plt.scatter(x, y, s=a, c=b, alpha=0.6, edgecolors='w', linewidths=1)
plt.title("Scatter Plot with Varying Colors and Sizes")
plt.show()

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# 1D data (only one feature)
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]

# Convert to 2D array (IMPORTANT)
data = np.array(x).reshape(-1, 1)

# Apply KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Plot (all points on same line → y = 0)
plt.scatter(x, [0]*len(x), c=kmeans.labels_)

# Plot centroids
plt.scatter(kmeans.cluster_centers_, [0]*len(kmeans.cluster_centers_), marker='x')

plt.title("K-Means Clustering (1D Data)")
plt.show()

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 3D data
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
z = [5, 3, 8, 2, 1, 9, 7, 4, 6, 8]

# Combine into dataset
data = np.array(list(zip(x, y, z)))

# Apply KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot data points
ax.scatter(x, y, z, c=kmeans.labels_)

# Plot centroids
centroids = kmeans.cluster_centers_
ax.scatter(centroids[:,0], centroids[:,1], centroids[:,2], marker='x')

ax.set_title("K-Means Clustering (3D)")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10, 30, 20])
ypoints = np.array([10, 250, 300])

print(xpoints, xpoints)

plt.plot(xpoints, ypoints)
plt.show()

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()