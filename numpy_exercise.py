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


# Q. array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
a = np.array([1, 2, 3])
np.r_[np.repeat(a, 3), np.tile(a, 3)]
np.repeat(a, 3)
np.tile(a, 3)


# Q. Get the common items between a and b
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
np.intersect1d(a, b)


# Q. From array a remove all items present in array b
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
np.setdiff1d(a, b)


# Q. Get the positions where elements of a and b match
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
np.where(a == b)


# Q. Get all items between 5 and 10 from a.
a = np.arange(15)
a[(a >= 5) & (a <= 10)]


# Q. Convert the function maxx that works on two scalars,
# to work on two arrays.
def maxx(x, y):
    if x > y:
        return x
    else:
        return y


pair_max = np.vectorize(maxx, otypes=[float])
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
pair_max(a, b)


# Q. Swap columns 1 and 2 in the array arr.
arr = np.arange(9).reshape(3, 3)
arr[:, [1, 0, 2]]


# Q. Swap rows 1 and 2 in the array arr:
arr = np.arange(9).reshape(3, 3)
arr[[1, 0, 2], :]


# Q. Reverse the rows/ columns of a 2D array arr
arr = np.arange(9).reshape(3, 3)
arr[::-1, ]
arr[:, ::-1]


# Q. Create a 2D array of shape 5x3 to contain random decimal numbers between
# 5 and 10
np.random.rand(5, 3) * 5 + 5
np.random.randint(low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
np.random.uniform(5, 10, size=(5, 3))


# Q. Print or show only 3 decimal places of the numpy array rand_arr.
rand_arr = np.random.random((5, 3))
np.set_printoptions(precision=3)
rand_arr


# Q. Pretty print rand_arr by suppressing the scientific notation (like 1e10)
np.random.seed(100)
rand_arr = np.random.random([3, 3])/1e3
rand_arr
np.set_printoptions(suppress=True, precision=6)
rand_arr


# Q. Limit the number of items printed in python numpy array a to a maximum
# of 6 elements.
np.set_printoptions(threshold=6)
a = np.arange(15)
a


# Q. Print the full numpy array a without truncating.
np.set_printoptions(threshold=6)
a = np.arange(6)
np.set_printoptions(threshold=np.nan)
a


# Q. Import the iris dataset keeping the text intact
url = 'https://archive.ics.uci.edu/ml/machine-learning-datab' \
      'ases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
iris[0:3, :]


# Q. Extract the text column species from the 1D iris imported
# in previous question.
print iris.shape
species = np.array([row[4] for row in iris])
species[:5]


# Q. Convert the 1D iris to 2D array iris_2d by omitting the species text field
url = 'https://archive.ics.uci.edu/ml/machine-' \
      'learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
iris_2d[:4]


iris_2d = np.genfromtxt(url, delimiter=',', dtype='float',
                        usecols=[0, 1, 2, 3])
iris_2d[:4]


# Q. Find the mean, median, standard deviation of iris's sepallength
# (1st column)
url = 'https://archive.ics.uci.edu/ml/machine-'\
      'learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
