# https://www.machinelearningplus.com/101-numpy-exercises-python/
# Q. Import numpy as `np` and print the version number.
import numpy as np
print np.__version__


# Q. Create a 1D array of numbers from 0 to 9
np.arange(0, 10, 1)


# Q. Create a 3×3 numpy array of all True’s
np.full((3, 3), True, dtype=bool)


# Q. Extract all odd numbers from arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1]


# Q. Replace all odd numbers in arr with -1
arr[arr % 2 == 1] = -1


# Q. Replace all odd numbers in arr with -1 without changing arr
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print arr
print out


# Q. Convert a 1D array to a 2D array with 2 rows
arr = np.arange(10)
arr.reshape((2, -1), order='C')


# Q. Stack arrays a and b vertically
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
np.concatenate((a, b), axis=0)  # method 1
np.vstack([a, b])


# Q. Stack the arrays a and b horizontally.
np.concatenate((a, b), axis=1)
np.hstack([a, b])
