import numpy as np


result = []


# newnode means the i+1 th row
def nextnode(pre_j_list, newnode, n):
    nex = [i for i in range(n)]
    nolist = []
    for i in range(len(pre_j_list)):
        nolist.append(pre_j_list[i] + (newnode - i))
        nolist.append(pre_j_list[i] - (newnode - i))
        nolist.append(pre_j_list[i])
    return list(np.setdiff1d(np.array(nex), np.array(nolist)))


def dfs(newnode, j, n, pre_j_list):
    pre_j_list.append(j)
    if newnode == n-1:
        result_list = [[i, pre_j_list[i]] for i in range(n)]
        temp = [[0 for _ in range(n)] for _ in range(n)]
        for x in result_list:
            temp[x[0]][x[1]] = 1
        result.append(temp)
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


nqueen(8)

len(result)
result[0]
result[1]
result[2]
