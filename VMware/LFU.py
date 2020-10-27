"""
460. LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity,
 it should invalidate the least frequently used item before inserting a new item.
  For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
  the least recently used key would be evicted.

"""
from collections import defaultdict
from collections import OrderedDict

"""
key2node dic: to store key -> Node(value, count)
count2node dic: store count --> OrderedDict[ key -> Node]
count  key  Node
1       1    (1,1)
        2    (2,1)
        

\\ get:
    1. check key2node exist?
        not return -1
    2. update count:
        get node from key2node
        del node in count2node by count
        
        update this count
        update mincount
        add node in count2node by new count
        
        return val
        
\\ put:
    1. use get key to check key2node exist?
        ### get key already update count!!!#####
        if yes update val
        :return
        
    2. if no:
        !!check capacity
            if >
                del node by mincount & LRU by popout first ele in OrderedDict
                
        create node for key, val, fre
        update mincount
        add to 2 dic
        return 

"""
class Node:
    def __init__(self, val, count):
        self.val = val
        self.count = count

class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keytoNodeDict = defaultdict()
        self.counttoOrderedDict = defaultdict(OrderedDict)
        self.minCount = -1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keytoNodeDict:
            return -1
        node = self.keytoNodeDict[key]
        ordered = self.counttoOrderedDict[node.count]
        del ordered[key]
        # update key count !
        # check whether need to update mincount
        if not ordered and node.count==self.minCount:
            self.minCount +=1
        node.count += 1
        # add to ordered
        self.counttoOrderedDict[node.count][key] = node
        return node.val



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # use get logic to update count and key
        if self.get(key) != -1:
            n = self.keytoNodeDict[key]
            n.val  = value
            return
        if self.capacity == 0:
            return
        # check capacity
        if len(self.keytoNodeDict)==self.capacity:
            # dele LFU & LRU in both dic
            ordered = self.counttoOrderedDict[self.minCount]
            # delete from top of list
            k, val = ordered.popitem(last=False)
            del self.keytoNodeDict[k]
        # create new node
        node = Node(value, 1)
        self.keytoNodeDict[key] = node
        self.counttoOrderedDict[node.count][key] = node
        self.minCount = 1



# class Node:
#     def __init__(self, value, freq):
#         self.value = value
#         self.freq = freq
#
#
# class LFU:
#     def __init__(self, cap: int):
#         self.freq = defaultdict(OrderedDict)
#         # hashmap to store nodes(contain values)
#         self.d = {}
#         self.minfreq = -1
#         self.cap = cap
#
#     def get(self, key: int) -> int:
#         if key not in self.d:
#             return -1
#         n = self.d[key]
#         od = self.freq[n.freq]
#         del od[key]
#         if not od and self.minfreq == n.freq:
#             self.minfreq += 1
#         n.freq += 1
#         od = self.freq[n.freq]
#         od[key] = n
#
#         return n.value
#
#     def put(self, key: int, value: int) -> None:
#         if self.get(key) != -1:
#             self.d[key].value = value
#             return
#         if self.cap == 0:
#             return
#         if len(self.d) == self.cap:
#             od = self.freq[self.minfreq]
#             k, v = od.popitem(last=False)
#             del self.d[k]
#         n = Node(value, 1)
#         self.d[key] = n
#         self.freq[1][key] = n
#         self.minfreq = 1


# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
print(obj.get(3))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))





class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        del self.count2node[node.count][key]

        # clean memory
        if not self.count2node[node.count]:
            del self.count2node[node.count]

        node.count += 1
        self.count2node[node.count][key] = node

        # NOTICE check minCount!!!
        if not self.count2node[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.cap:
            return

        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key)  # NOTICE, put makes count+1 too
            return

        if len(self.key2node) == self.cap:
            # popitem(last=False) is FIFO, like queue
            # it return key and value!!!
            k, n = self.count2node[self.minCount].popitem(last=False)
            del self.key2node[k]

        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return