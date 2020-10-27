def formTeam(d, t, q):
    def curteam(curd, curt, length, n, i):

        if length == n and curd < d and curt < t:
            result[i] += 1
            return
        if curd < d - 1 and curt < t - 1:
            curteam(curd + 1, curt, length + 1, n, i)
            curteam(curd, curt + 1, length + 1, n, i)
        if curd == d - 1 and curt < t - 1:
            if curt<t-2:
                curteam(curd, curt + 1, length + 1, n, i)
            curteam(0, curt + 1, length + 1, n, i)
        if curt == t - 1 and curd < d - 1:
            if curd<d-2:
                curteam(curd+1, curt, length + 1, n, i)
            curteam(curd + 1, 0, length + 1, n, i)

        return

    result = [0] * len(q)

    for i, n in enumerate(q):
        if n == 1:
            result[i] = 2
            continue
        else:
            curteam(0, 0, 0, n, i)
    return result

# print(formTeam(2,4,[6] ))


