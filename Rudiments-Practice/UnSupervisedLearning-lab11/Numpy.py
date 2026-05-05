import numpy as np
print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(type(arr))
print(arr)

# dimenasions of arrays 
a = np.array(42)
b = np.array([1, 2, 3, 4,5])
c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
d = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 1.5], dtype='i')

print(arr.dtype)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]] ])
for x in np.nditer(arr):
    print(x)

arr = np.array([1, 2, 3, 4, 5, 6])
new = np.array_split(arr, 3)

print(new)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

arr = np.array([1, 2 ,3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0

new = arr[filter_arr]

print(filter_arr)
print(new)