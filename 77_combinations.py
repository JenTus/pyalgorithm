'''
Given two integers n and k,
return all possible combinations of k numbers out of 1 ... n.
'''


def combine(n, k):

    def combine_cur_left(current, left, k):
        if len(left)+len(current) < k:
            return 0
        if len(current) == k:
            combinelist.append(current)
            return 0
        for i in range(len(left)):
            temp_cur, temp_left = current[:], left[:][i+1:]
            temp_cur.append(left[i])
            combine_cur_left(temp_cur, temp_left, k)
        return 0

    combinelist = []
    combine_cur_left([], range(1, n+1), k)

    return combinelist

combine(5,2)
