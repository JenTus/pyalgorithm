'''
Given a set of distinct integers, nums,
return all possible subsets (the power set).
'''


def subsets(nums):

    def subsets_cur_left(current, left, k):
        if len(left)+len(current) < k:
            return 0
        if len(current) == k:
            combinelist.append(current)
            return 0
        for i in range(len(left)):
            temp_cur, temp_left = current[:], left[:][i+1:]
            temp_cur.append(left[i])
            subsets_cur_left(temp_cur, temp_left, k)
        return 0

    clist = []
    for k in range(len(nums) + 1):
        combinelist = []
        subsets_cur_left([], nums, k)
        clist.extend(combinelist)

    return clist

subsets([1,2,3])
