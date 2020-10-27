def minAvailableDuration(self, slots1, slots2, duration: int):
    slots1.sort()
    slots2.sort()
    i = 0
    j = 0
    ans = []
    while i<len(slots1) and j<len(slots2):
        head  = max(slots1[i][0],slots2[j][0] )
        tail = min(slots1[i][1], slots2[j][1])
        if head +duration<=tail:
            ans.append([head, tail])
        # Remove the interval with the smallest endpoint
        if slots1[i][1]<slots2[j][1]:
            i+=1
        else:
            j+=1

    return ans