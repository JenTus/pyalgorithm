# if len(left) == 0, permutelist.append(current)
def permute(nums):

    def permute_cur_left(current, left):
        if len(left) == 0:
            permutelist.append(current)
            return 0
        for i in range(len(left)):
            temp_cur, temp_left = current[:], left[:]
            temp_cur.append(left[i])
            temp_left.pop(i)
            permute_cur_left(temp_cur, temp_left)
        return 0

    permutelist = []
    permute_cur_left([], nums)

    return permutelist


permute([0, 0, 3])
