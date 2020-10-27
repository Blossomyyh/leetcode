""""

https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516968/JavaC%2B%2BPython-Easy-and-Concise

Assume we have already n - 1 pairs, now we need to insert the nth pair.
To insert the first element, there are n * 2 - 1 chioces of position。
To insert the second element, there are n * 2 chioces of position。
So there are (n * 2 - 1) * n * 2 permutations.
Considering that delivery(i) is always after of pickup(i), we need to divide 2.
So it's (n * 2 - 1) * n.

"""
"""
k - pair
\\ when k = 1 , res = 1
\\ f(k) = f(k-1) * (2k -2+1)*(2k -1+1)//2   mod(10**9+7)

"""
def countOrders(self, n):
    res, mod = 1, 10 ** 9 + 7
    for i in range(2, n + 1):
        res = res * (i * 2 - 1) * (i * 2) / 2 % mod
    return res

def printpD(n):
    res = []
    def dfs(p, d, cur):
        if len(cur)==4*n:
            res.append(cur)
            return
        if len(p)<n:
            for i in range(1,n+1):
                if i not in p:
                    dfs(p+[i], d, cur+"P"+str(i))
        if len(d)<n and len(p)>len(d):
            for i in range(1,n+1):
                if i not in d and i in p:
                    dfs(p, d+[i], cur+"D"+str(i))
    dfs([],[],"")

    print(res)


    
    stack = [([],[], "")]
    res2 = []
    while stack:

        p,d,cur = stack.pop()
        if len(cur)==4*n:
            res2.append(cur)
        if len(p)<n:
            for i in range(1,n+1):
                if i not in p:
                    stack.append((p+[i], d, cur+"P"+str(i)))
        if len(d)<n and len(p)>len(d):
            for i in range(1,n+1):
                if i not in d and i in p:
                    stack.append((p, d+[i], cur+"D"+str(i)))
    print(res2)

    return
print(printpD(3))

