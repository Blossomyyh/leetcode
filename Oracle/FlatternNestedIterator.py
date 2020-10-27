# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        define function flattenList(nestedList):
            for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                append nestedInteger.getInteger() to integers
            else:
                recursively call flattenList on nestedInteger.getList()
        :param nestedList:
        """
        self.integers = []
        self.pos = -1
        def flattern(nested):
            for i in nested:
                if i.isInteger():
                    self.integers.append(i.getInteger())
                else:
                    flattern(i.getList())
        flattern(nestedList)


    def next(self) -> int:
        self.pos +=1
        return self.integers[self.pos]

    def hasNext(self) -> bool:
        return self.pos +1<len(self.integers)
