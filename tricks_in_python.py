# comprehension syntax in python
# python generator
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
G = (sum(row) for row in M)
next(G)
next(G)
next(G)
next(G)  # error
list(map(sum, M))


# How to creat a dictionary
dict(zip([1, 2], [3, 4]))
dict(aa=2, bb=4)  # can not replace aa with 1 and bb with 2
dict(name='Bob', job='dev', age=40)


# tuples are immutable
T = (1, 2, 3, 4)
T = T + (5, 6)
T
T[0] = 2  # error
T = (2, ) + T[1:]
T


# assign copies to other variables
L = [1, 2, 3]
D = {"a": 1, "b": 2}
A = L[:]
B = D.copy()


# Gotchas COPY?
L = [1, 2, 3]
M = ['X', L, 'Y']
N = ['X', L[:], 'Y']
M
L[1] = 0
M
N


# impact Y but not X and YY
L = [4, 5, 6]
X = L * 4
X
Y = [L] * 4
Y
YY = [list(L)] * 4
YY
L[1] = 0
X
Y
YY


# raise and assert
