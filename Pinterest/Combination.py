"""
combination： abC -> AbC, aBC, abC, ABC.
only need lower case to upper case
output list of possibilities
"""

"""
\\ backtracking
creat fun (list, idx):
    if idx == len(list) -1:
        append this sequence
    
    list[idx]-> upper case
    for i in range idx, last:
        if list[i] is lower case:
            backtracking(list add uppercase, i)
        
fun(list, 0)
"""

def UpperCombination(arr):
    if not arr: return []
    result = []

    def backtracking(idx, curlist):
        if len(curlist) == len(arr):
            result.append(curlist[:])
            print("curlist",curlist)
        #
        for i in range(idx, len(arr)):
            # print(arr[i])
            if arr[i].islower():
                print("backtracking", curlist + [arr[i].upper()])
                backtracking(i+1, curlist + [arr[i].upper()])

            backtracking(i + 1, curlist + [arr[i]])
            print(curlist)
    backtracking(0, [])

    return result

print(UpperCombination('abCd'))
