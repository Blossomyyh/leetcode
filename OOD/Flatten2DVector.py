class Vector2D:

    def __init__(self, v:[[int]]):
        self.list = []
        for item in v:
            self.list.extend(item)
        self.p = -1

    def next(self) -> int:
        if self.hasNext():
            self.p+=1
            return self.list[self.p]

    def hasNext(self) -> bool:
        if self.p <len(self.list)-1:
            return True
        else:
            return False


"""
Constructor: O(N + V)O(N+V).

In total, we'll append NN integers to the nums list. Each of these appends is an O(1)O(1) operation. This gives us O(N)O(N).

Something to be cautious of is that inner vectors don't have to contain integers. Think of a test cases such as [[], [2], [], [], []]. For this test case, N = 1N=1, because there's only one integer within it. However, the algorithm has to loop through all of the empty vectors. The cost of checking all the vectors is O(V)O(V).

Therefore, we get a final time complexity of O(N + V)O(N+V).

next(): O(1)O(1).

All operations in this method, including getting the integer at a specific index of a list, are O(1)O(1).

hasNext(): O(1)O(1).

Space complexity : O(N)O(N).

"""

class Vector:
    def __init__(self, v: [[int]]):
        self.vector = v
        self.inner = 0
        self.outer = 0

        # If the current outer and inner point to an integer, this method does nothing.
        # Otherwise, inner and outer are advanced until they point to an integer.
        # If there are no more integers, then outer will be equal to vector.length
        # when this method terminates.
    def advance_to_next(self):
        while self.outer <len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0

    def hasNext(self) ->int:
        self.advance_to_next()
        return self.outer<len(self.vector)

    def next(self)->int:
        if self.hasNext():
            # Return current element and move inner so that is after the current
            # element.
            result = self.vector[self.outer][self.inner]
            self.inner += 1
        return result
"""
Time complexity.

Constructor: O(1)O(1).

next() / hasNext(): O(v/n) or O(1).

Space O(1).
"""
