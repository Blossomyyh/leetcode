"""
abcbads   ads
start 4
end 4
dictionary: a - 4
            d - 5  s - 6



1. 0-7 -> 2-9

18 -> 2, 0
8 -> 1, 0
98/99/998 -> 1, 0, 0
2. 8 -> +1 0
3. 9 -> +1 1
"""


def addTwo(integers):
    # edge case
    if not integers:
        return []
    # normal case
    if 0 <= integers[-1] <= 7:
        integers[-1] += 2
    elif integers[-1] in [8, 9]:
        cur = integers[-1] + 2
        carrier, cur = divmod(cur, 10)
        integers[-1] = cur
        p = len(integers) - 2
        # print(integers, p, cur, carrier)
        while 0 <= p < len(integers) - 1 and carrier == 1:
            print(integers, p, carrier)
            if integers[p] == 9:
                integers[p] = 0
                carrier = 1
            else:
                integers[p] += carrier
                carrier = 0
                break
            p -= 1
        if carrier == 1:
            integers.insert(0, 1)
    return integers


# print(addTwo([7]))
print("_______")
print(addTwo([1, 8]))
print("_______")
print(addTwo([9, 8]))