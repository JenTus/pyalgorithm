# whether the knight can cover the chess-board without revisiting the same
# location
import numpy as np


def nextnode(i, j):
    nextlist = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1],
                [2, 1]]
    nn = [[i + x[0], j + x[1]] for x in nextlist]
    return nn


# dfs
# [i,j], next i+/-1/2 j-/+2/1
def dfs(i, j):
    if np.sum(board) == m*n:  # filled
        print "Success!"
        return 0
    elif (i >= m) | (i < 0) | (j >= n) | (j < 0):
        return 1
    elif board[i][j] == 1:
        return 1
    else:
        board[i][j] = 1
        locationlist.append([i, j])
        nextnodelist = nextnode(i, j)
        for x in nextnodelist:
            if dfs(x[0], x[1]) == 0:
                return 0
        [prei, prej] = locationlist.pop()
        board[prei][prej] = 0
        if len(locationlist) == 0:
            return "failed"
        else:
            return 1


def route(i, j):
    if dfs(i, j) == 0:
        for v in range(len(locationlist)):
            board[locationlist[v][0]][locationlist[v][1]] = v+1
    else:
        "route does not exist"


m = 8
n = 8
board = [[0 for _ in range(m)] for _ in range(n)]
locationlist = []
beginnode = [3, 4]
route(beginnode[0], beginnode[1])
board
len(locationlist)
