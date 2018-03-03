import numpy as np


# newnode means the i+1 th row
def nextnode(pre_j_list, newnode, n):
    nex = [i for i in range(n)]
    pp = [[i, pre_j_list[i]] for i in range(len(pre_j_list))]
    nn = [[x, x + (newnode - i), x - (newnode - i)] for [i, x] in pp]
    nolist = reduce((lambda i, j: i + j), nn)
    return list(np.setdiff1d(np.array(nex), np.array(nolist)))


def dfs(newnode, j, n, pre_j_list):
    pre_j_list.append(j)
    if newnode == n-1:
        result_list = [[i, pre_j_list[i]] for i in range(n)]
        temp = [["." for _ in range(n)] for _ in range(n)]
        for x in result_list:
            temp[x[0]][x[1]] = "Q"
        result.append(["".join(x) for x in temp])
        pre_j_list.pop()
        return 0
    else:
        next_j_list = nextnode(pre_j_list, newnode + 1, n)
        if len(next_j_list) == 0:
            pre_j_list.pop()
            return 1
        for next_j in next_j_list:
            dfs(newnode + 1, next_j, n, pre_j_list)
        pre_j_list.pop()
        return 1


def nqueen(n):
    for j in range(n):
        dfs(0, j, n, [])


result = []
nqueen(9)


len(result)
result
result[0]
result[1]
result[2]
  
