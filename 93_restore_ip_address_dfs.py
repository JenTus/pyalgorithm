# test valid
def test_valid(s):
    if int(s) <= 255:
        return True
    else:
        return False


# get the next valid number ranging from 0 to 255
# from the remaining string
def next_valid_num(remain_string):
    next_num_list = []
    left_string_list = []
    for i in range(1, len(remain_string)+1):
        if test_valid(remain_string[:i]):
            next_num_list.append(int(remain_string[:i]))
            left_string_list.append(remain_string[i:])
        else:
            break
    return [next_num_list, left_string_list]


#
def dfs(remain_string, currentlist):
    if len(currentlist) == 4:
        if len(remain_string) == 0:
            valid_ip_list.append(currentlist)
        return 0
    next_num_list, left_string_list = next_valid_num(remain_string)
    if len(next_num_list) == 0:
        return 0
    else:
        for i in range(len(next_num_list)):
            next_num = next_num_list[i]
            next_string = left_string_list[i]
            # print next_num, next_string
            dfs(next_string, currentlist[:] + [next_num])
    return 0


def changee_valid_ip_form(valid_ip, s):
    ip_str = []
    for valid in valid_ip:
        need_check_0 = ".".join([str(x) for x in valid])  # eg."001"
        if len(need_check_0) - 3 == len(s):
            ip_str.append(need_check_0)
    return ip_str


valid_ip_list = []
dfs("101023", [])
changee_valid_ip_form(valid_ip_list, "101023")
