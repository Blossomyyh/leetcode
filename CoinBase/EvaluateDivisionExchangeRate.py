"""
399. Evaluate Division

Exchange rate for currencies
"""
"""
\\ defaultdict(defaultdict) to store pairs and rates

1. edge case: check in dic
2. backtracking to find the way from a->b

    maintain a set & currate
    make default as add --> -1.0
    for every neighbour in dic[a]:
        check not in set:
            add update 
                check add != 1.0:
                    find the way and break
    # base case
    a==b return currex

\\ Time Complexity: O(M⋅N)
 N be the number of input equations and M be the number of queries.
 Space Complexity: O(N)
 
"""

print("a/b"[::-1])
from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # c/d = c/a * a/d ...

        # 1. build map for each pair & relation of pair
        dic = defaultdict(defaultdict)
        for i, m in enumerate(equations):
            a = m[0]
            b = m[1]
            dic[a][b] = values[i]
            dic[b][a] = 1.0/values[i]

        def checkValid(a):
            return a in dic
        # backtracking to search for exchange rate
        def exchangerate(a, b, currex, curset, i):
            if a == b:
                if res[i]<currex:
                    res[i] = currex
                return
            else:
                for neigh in dic[a]:
                    if neigh not in curset:
                        curset.add(neigh)
                        exchangerate(neigh, b, currex*dic[a][neigh], curset,i)
                        curset.remove(neigh)
            return

        res = [-0.1]*len(queries)
        for i, (a, b) in enumerate(queries):

            if checkValid(a) and checkValid(b):
                exchangerate(a, b, 1.0, set(), i)
        print(res)
        return res



    def unionfindway(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # c/d = c/a * a/d ..

        # build graph to store parent of current node
        gidweight = {}

        def find(nodeid):
            if nodeid not in gidweight:
                # initialize a group
                gidweight[nodeid] = (nodeid, 1.0)
            # get groupid and weight of node in the group
            gid, nodeweight = gidweight[nodeid]
            if nodeid != gid:
                # find last weights
                newgid, groupweight = find(gid)
                # update weights and groups
                gidweight[nodeid] = (newgid, nodeweight*groupweight)
            return gidweight[nodeid]

        def union(divident, divisor, value):
            dividentgid, dividentweight = find(divident)
            divisorgid, divisorweight = find(divisor)
            if dividentgid != divisorgid:
                # merge 2 group together, update dict
                """ # by attaching the dividend group to the one of divisor """
                gidweight[dividentgid] = (divisorgid, divisorweight*value / dividentweight)

                # Step 1). build the union groups
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        res = []
        # Step 2). run the evaluation, with "lazy" updates in find() function
        for (dividend, divisor) in equations:
            if dividend not in gidweight or divisor not in gidweight:
                res.append(-0.1)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                # case 2). the variables do not belong to the same chain/group
                    res.append(-1.0)
                else:
                    res.append(dividend_weight/divisor_weight)
        return res


        print(gidweight)


equations = [["a","b"],["b","c"],["a","m"], ["m","c"]]
values = [2.0,3.0,8.0,2.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

Solution().calcEquation(equations, values, queries)




import urllib.request
import json
url = "https://api.pro.coinbase.com/products"
# Open the URL as Browser, not as python urllib
page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
infile=urllib.request.urlopen(page).read()
data = json.loads(infile)
print(data)

def getRate(id):
    url = "https://api.pro.coinbase.com/products"+"/"+id+"/ticker"
    print(url)
    # Open the URL as Browser, not as python urllib
    page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    infile = urllib.request.urlopen(page).read()
    data = json.loads(infile)
    return data

"""
dictionary
    btc-usd-990
    usd-btc-0.0001
backtracking
    find all possible ways
input:[['btc-usd', 1000, 990]]
output: float
assume : input all valid

real API
"""
from collections import defaultdict


class exchange:
    def __init__(self):
        super().__init__()
        self.maxrate = 0

    def currencyExchange(self, tickers, base_currency, base_amount, quote_currency):
        # step 1: build dictionary to store relations and rates
        dictionary = defaultdict(defaultdict)
        for ticker in tickers:
            currency1, currency2 = ticker[0].split('-')
            dictionary[currency1][currency2] = ticker[2]
            dictionary[currency2][currency1] = 1.0 / ticker[1]
        print(dictionary)

        # step 2: backtracking
        def backtracking(base_currency, quote_currency, currate, curset):
            # base case
            if base_currency == quote_currency:
                # update
                if self.maxrate < currate:
                    self.maxrate = currate
            else:
                # keep backtracking
                for neighbour in dictionary[base_currency]:
                    if neighbour not in curset:
                        curset.add(neighbour)
                        backtracking(neighbour, quote_currency, currate * dictionary[base_currency][neighbour], curset)
                        curset.remove(neighbour)
            return

        # call backtracking
        backtracking(base_currency, quote_currency, 1.0, set())
        return self.maxrate * base_amount


task = exchange()
tickers = []
for item in data:
    id = item['id']
    info = getRate(id)
    bid = info['bid']
    ask = info['ask']
    tickers.append([id, ask, bid])
print(tickers)
# tickers = [
#     ['BTC-USD', 1000, 990],
#     ['BTC-EUR', 1200, 1150],
#     ['ETH-USD', 200, 180],
#     ['ETH-EUR', 220, 210],
#     ['BTC-ETH', 5.6, 5.5]
# ]
base_currency = 'USD'
base_amount = 100
quote_currency = 'EUR'

print(task.currencyExchange(tickers, base_currency, base_amount, quote_currency))
