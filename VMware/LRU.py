"""
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

"""
\\ SOl: OrderedDict in python
put: 
    check the length of dic
    if > k then, delete the first key(LRU)
    append key value at the end of the dictionary
get:
    get from dic & move to end (LRU)
    
"""

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    '''
    void put(int key, int value) Update the value of the key if the key exists. 
    Otherwise, add the key-value pair to the cache. 
    If the number of keys exceeds the capacity from this operation, 
    evict the least recently used key.
    '''

    '''
    1. not key: -1
    2. have key: update position -> most recentely
        return value
    '''
    def get(self, key: int) -> int:
        print(self.cache)
        if key not in self.cache:
            return -1
        else:
            # update key to the end
            self.cache.move_to_end(key)
            return self.cache[key]

    '''
    1. update -- move to end
        / insert key -- add to end
    2. if > k
        delete top -- popitem(last=False)
    
    '''
    def put(self, key: int, value: int) -> None:
        # update the key first/insert --> based on capacity --> delete
        # insert it to end / Update some key
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            #  pop it from top
            self.cache.popitem(last=False)


"""
\\ SOL; Hashmap + DoubleLinkedList

hashmap --> record key and node!!! --> no need to search for node

DoubleLinkedList --> manage sequence

(head, tail, count)
    \\ _add_node   insertion/add key: add to head.next
    \\ _pop_tail deletion: delete tail.prev -- (Least recently used)
    \\ _move_to_head: update the key(dele+add)
    \\ _delete_node: change the pointers for prev and next node
"""
class ListNode:
    def __init__(self, key: int, val:int, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

from collections import defaultdict
class LRUCache:
    def _add_node(self, node):
        # insert from start
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _pop_tail(self):
        # delete the end
        last = self.tail.prev
        self._delete_node(last)
        return last

    def _move_to_head(self, node):
        # search and return this node
        self._delete_node(node)
        self._add_node(node)

    def _delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def __init__(self, capacity: int):
        self.cache = defaultdict(int)
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0,None, self.head)
        self.head.next = self.tail
        self.count = 0

    def get(self, key: int) -> int:
        # store all the nodes in the dict and get it from dictionary
        # no need to search for it!
        node = self.cache.get(key, None)
        if not node:
            return -1
        else:
            # update key to the end
            self._move_to_head(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if not node:
            newnode =  ListNode(key, value, None, None)
            self.cache[key] = newnode
            self._add_node(newnode)
            self.count+= 1
        else:
            node.val = value
            self._move_to_head(node)

        if self.count>self.capacity:
            # pop out tail from list and del it in dict
            last = self._pop_tail()
            del self.cache[last.key]
            self.count-=1

lru = LRUCache(2)
lru.put(1,1)
lru.put(2,1)
lru.put(3,1)
lru.get(2)



