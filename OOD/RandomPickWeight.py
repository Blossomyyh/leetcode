"""
For the pickIndex() function, here are the steps that we should perform.

Firstly, we generate a random number between 0 and 1.
We then scale up this number, which will serve as our target offset.

We then scan through the prefix sums that we generated before by linear search,
to find the first prefix sum that is larger than our target offset.

And the index of this prefix sum would be exactly the right place that the target should fall into.
We return the index as the result of pickIndex() function.
"""
import random
class Solution:

    def __init__(self, w):
        self.sums = []
        prefixsum = 0
        for we in w:
            prefixsum += we
            self.sums.append(prefixsum)
        self.total = prefixsum
    def pickIndex(self) -> int:
        # random.random() from0-1
        t = self.total * random.random()
        for i, pre in enumerate(self.sums):
            if t<pre:
                return i