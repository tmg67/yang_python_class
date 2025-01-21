import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(type(arr))

import numpy as np

print("1 D array", arr)

arr = np.array([1, 2, 3, 4, 5])



array_sum = arr.sum()
print("sum of all the element is:", array_sum)
array_mean = arr.mean()
print("mean is :", array_mean)
array_std = arr.std()
print("the standard deviation is:", array_std)
array_multiplication = arr * 2 
print("the multiplication by 2 of all the elements is:", array_multiplication)


print(type(arr))