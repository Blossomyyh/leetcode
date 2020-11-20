"""
284. Peeking Iterator

Given an Iterator class interface with methods: next() and hasNext(),
design and implement a PeekingIterator that support the peek() operation
 -- it essentially peek() at the element that will be returned by the next call to next().
"""

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._next = iterator.next()
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        if self._next is None:
            raise StopIteration()
        val = self._next
        self._next = None
        if self.iterator.hasNext():
            self._next = self.iterator.next()
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next is not None


        # Your PeekingIterator object will be instantiated and called as such:
        # iter = PeekingIterator(Iterator(nums))
        # while iter.hasNext():
        #     val = iter.peek()   # Get the next element but not advance the iterator.
        #     iter.next()         # Should return the same value as [val].


        # Your PeekingIterator object will be instantiated and called as such:
        # iter = PeekingIterator(Iterator(nums))
        # while iter.hasNext():
        #     val = iter.peek()   # Get the next element but not advance the iterator.
        #     iter.next()         # Should return the same value as [val].

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """