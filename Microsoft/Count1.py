"""
count 1
"""
def NumberOf1(self, n):
    count = 0
    while n&0xffffffff != 0:
        count += 1
        n = n & (n-1)
    return count


"""
M to N
"""
def numMtoN(num, m, n):
    s = list(map(int, str(num)))

    dec = 0
    for i in s[::]:
        dec *= m
        dec += i

    # dec to N
    mid = 0
    while (dec != 0):
        mid *= 10
        mid += (dec % n)
        dec //= n

    # 逆序
    res = 0
    while (mid != 0):
        res *= 10
        res += (mid % 10)
        mid //= 10

    return res