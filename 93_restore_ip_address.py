'''
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

brute force
'''


# reserved ip lists that can not be used
a = [[[10, 0, 0, 0], [10, 255, 255, 255]],
     [[172, 16, 0, 0], [172, 31, 255, 255]],
     [[192, 168, 0, 0], [192, 168, 255, 255]]]


# test if a ip address is valid
def test_validity(ip_address):
    for ip in ip_address:
        if ip > 255:
            return False
    for i in range(len(a)):
        flag = 0
        for j in range(len(a[0][0])):
            if (a[i][0][j] > ip_address[j]) | (a[i][1][j] < ip_address[j]):
                flag = 1
        if flag == 0:
            return False
    return True


# chagne a string into a ipaddress list
# according to the index
def change_str_iplist(s, i, j, k):
    return [int(s[:i]), int(s[i:j]), int(s[j:k]), int(s[k:])]


def get_valid_iplist(s):
    need_check_ip = []
    valid_ip = []
    ls = len(s)
    for i in range(1, 4):
        for j in range(i+1, i+4):
            if j + 1 < ls:
                for k in range(j+1, ls):
                    need_check_ip.append(change_str_iplist(s, i, j, k))
    # print "need_check_ip is: " + str(need_check_ip)
    for check_ip in need_check_ip:
        if test_validity(check_ip):
            valid_ip.append(check_ip)

    return valid_ip


# chagne valid ip into str.str.str.str form
def chagne_valid_ip_form(valid_ip):
    ip_str = []
    for valid in valid_ip:
        ip_str.append(".".join([str(x) for x in valid]))
    return ip_str


valid_ip = get_valid_iplist("25525511135")
chagne_valid_ip_form(valid_ip)
