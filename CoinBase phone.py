# Offers to BUY: 100, 100, 99, 99, 97, 90
# Offers to SELL: 109, 110, 110, 114, 115, 119
"""
maxheap -- buy offers

minheap -- sell offers
 buy -> min

 in 10 min
 list 10 ele
 buy -> 1min 1%10 -> [1] in list of buys


"""
import heapq
from collections import defaultdict


class Match:
    def __init__(self, buyOffer, sellOffer):
        # time: nlogn
        super().__init__()
        # maxheap -- buy offers
        self.buydict = defaultdict(list)
        self.selldict = defaultdict(list)
        for i in buyOffer:
            self.buydict[float('inf')].append(i)
        for i in sellOffer:
            self.selldict[float('inf')].append(i)
        print(self.buydict)
        print(self.selldict)

    def checkExpire(self, curtime):
        for key in self.buydict:
            if key < curtime:
                del self.buydict[key]
        for key in self.selldict:
            if key < curtime:
                del self.selldict[key]

    def addSellOffer(self, sellOffer, curtime):
        # time O(logn)
        # find max buy in buy offers
        self.checkExpire(curtime)
        heap = []
        for buylist in self.buydict:
            for buys in self.buydict[buylist]:
                heapq.heappush(heap, -buys)

        maxbuy = - heapq.heappop(heap)
        if maxbuy >= sellOffer:
            print(str(sellOffer) + "sell offer matches to :" + str(maxbuy))
            return maxbuy
        else:
            self.selldict[curtime].append(sellOffer)
            print("No best match yet.")
            print("list of sells: ", self.selldict)
            return

    def addBuyOffer(self, buyOffer):
        # find min sell in sell offers
        minSell = heapq.heappop(self.sell)
        if minSell <= buyOffer:
            print(str(buyOffer) + " buy offer matches to :" + str(minSell))
            return minSell
        else:
            heapq.heappush(self.sell, minSell)
            heapq.heappush(self.buy, -buyOffer)
            print("No best match yet.")
            print("list of buys: ", self.buy)
            return


buyOffer = [100, 100, 99, 99, 97, 90]
sellOffer = [109, 110, 110, 114, 115, 119]

match = Match(buyOffer, sellOffer)
print(match.addSellOffer(150, 1))

# print(match.addBuyOffer(109))


"""
You operate a marketplace for buying & selling used textbooks. For a given textbook, e.g. “Theory of Cryptography,” there are people who want to buy this textbook and people who want to sell.

Offers to BUY: $100, $100, $99, $99, $97, $90
Offers to SELL: $109, $110, $110, $114, $115, $119

A match occurs when two people agree on a price. Some new offers do not match. These offers should be added to the active set of offers. For example:
Tim offers to SELL at $150. This will not match. No one is willing to buy at that price so we save the offer.
Offers to SELL:: $109, $110, $110, $114, $115, $119, $150

When matching we want to give the customer the “best price”. Example matches:

If Jane offers to BUY at $120, she will match and buy a book for $109 (the lowest offer to sell is the best price). The sell offers should be updated to reflect the match
Offers to SELL: $110, $110, $114, $115, $119, $150

If Connie offers to SELL at $99 she will match and sell her book for $100 (the highest offer to buy is the best price). The buy offers should be updated to reflect the match
Offers to BUY: $100, $99, $99, $97, $90

Our system will need to:
Accept incoming offers to buy & sell
Output if the price matches
Keep an updated collections of buys & sells


Follow up: 实现会expire的 order，比如说buyer 的一个order valid for 10 min，然后自动expire

"""

"""
我用了两个heap， 
MaxHeap来存Buy Offer， 
MinHeap来存Sell Offer， 
每次request进来，
如果是 buy 就看 MinHeap顶端，小于buy的价格就可以匹配，
然后移除MinHeap顶端； 若不是， 则将buy offer 加入MaxHeap
"""



