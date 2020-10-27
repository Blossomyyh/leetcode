from collections import defaultdict
def showString(s):
    if not s:
        return ""
    res  = ""
    count = defaultdict(int)
    for char in s:
        count[char] = count.get(char, 0) + 1
    sortlist = sorted(count.items(), key=lambda x: x[1])
    # print(sortlist)
    for k, v in sortlist:
        res = k*v + res
    return res
print(showString("abbc"))
print(showString(""))
print(showString("abbbbccccssjj"))