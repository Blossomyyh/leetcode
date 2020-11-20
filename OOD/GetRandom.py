"""
380. Insert Delete GetRandom O(1)
O(1) time space O(n)

* random.randrange(start=  Default 0, stop, step = Default 1)

* random.randint(3, 9) -- print 3-9 both included
    This method is an alias for randrange(start, stop+1).

* random.random() method returns a random floating number between 0 and 1.

* random.choice(self.list)
    return element in this list
"""
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.setlist = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.setlist :
            return False
        self.setlist.add(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.setlist :
            return False
        self.setlist.remove(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        ran = random.randint(0, len(self.setlist)-1)
        return list(self.setlist)[ran]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""

\\ duplication 
\\ time O(1)

insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.

getRandom: Returns a random element from current collection of elements. 
The probability of each element being returned is linearly related to 
    the number of same value the collection contains.
"""

from collections import defaultdict
from random import choice
class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        # remember the idx in the list
        self.list.append(val)
        self.idx[val].add(len(self.list) - 1)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]:
            return False
        # get remove idx & idx of last ele in list
        #set.pop() get last element in set
        remove, last = self.idx[val].pop(), self.list[-1]
        # swap last ele to this position
        # save remove idx to last element in dic
        self.list[remove] = last
        self.idx[last].add(remove)
        # discard len-1 in last element
        self.idx[last].discard(len(self.list)-1)
        # delete this element
        self.list.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list)



        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()