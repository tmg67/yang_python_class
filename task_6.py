import numpy


arr = numpy.array([1, 2, 3, 4, 5])

print(type(arr))

import numpy as np

print("1 D array", arr)

arr = np.array([1, 2, 3, 4, 5])

print("2 D array", arr)


a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3], [4,5,6]])
d = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(type(arr))

A = np.array([[2, 2 ],[1, 0]])
B = np.array([[1, 3 ],[1, 0]])

C = (A@B)
print(C)