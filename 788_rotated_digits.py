range(1, -2, -1)
aa = "abdgw"

len(aa)
[aa[i] for i in range(len(aa)-1, -1, -1)]

range(1, 3+1, 1)


def reverse(s):
    if s == "2":
        return "5"
    elif s == "5":
        return "2"
    elif s == "6":
        return "9"
    elif s == "9":
        return "6"
    elif (s == "0") or (s == "1") or (s == "8"):
        return s
    else:
        return "00"


def rotatedDigits(N):
    goodlist = []
    for n in range(1, N + 1, 1):
        sn = str(n)
        newlist = [reverse(i) for i in sn]
        new = ''.join(newlist)
        if (len(new) == len(sn)) & (sn != new):
            goodlist.append(n)
    return goodlist


[reverse(i) for i in "3333"]
rotatedDigits(857)
