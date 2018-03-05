'''
The gray code is a binary numeral system where two successive values differ
in only one bit.

Given a non-negative integer n representing the total number of bits in the
code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
'''


def grayCode(n):
    if n == 0:
        return [0]
    for i in range(1, n+1):
        if i == 1:
            graycode = [0, 1]
        else:
            graycode += [2**(i-1) + x for x in graycode[::-1]]
    return graycode


grayCode(2)
