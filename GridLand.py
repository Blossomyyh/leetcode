"""
start -> end
present minimum path with H V (horizontal vertical)

F x x
x x x
x x F

"""
def gridLand(first, final):
    r = final[0] - first[0]
    c = final[1] - first[1]
    res = []
    def iteration(cur, ru, cu):
        if ru==r and c ==cu:
            res.append(cur)
        else:
            if ru<r:
                iteration(cur+"H", ru+1, cu)
            if cu<c:
                iteration(cur+"V", ru, cu+1)

    iteration("", 0, 0)

    return res
print(gridLand([0,0], [1,1]))