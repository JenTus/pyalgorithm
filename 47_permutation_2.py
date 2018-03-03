# permuteUnique(nums)


# if len(left) == 0, permutelist.append(current)
def permuteUnique(nums):

    def test(item, left, index):
        if item in left[:index]:
            return False
        return True

    def permute_cur_left(current, left):
        if len(left) == 0:
            permutelist.append(current)
            return 0
        for i in range(len(left)):
            temp_cur, temp_left = current[:], left[:]
            item = temp_left[i]
            if test(item, temp_left, i):
                temp_left.pop(i)
                temp_cur.append(item)
                permute_cur_left(temp_cur, temp_left)
            else:
                continue
        return 0

    permutelist = []
    permute_cur_left([], nums)

    return permutelist


permuteUnique([0, 0, 3])
