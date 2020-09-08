# For each asteroid, the absolute value represents its size,
# and the sign represents its direction (positive meaning right,
# negative meaning left). Each asteroid moves at the same speed.

"""
A row of asteroids is stable if no further collisions will occur.
After adding a new asteroid to the right, some more collisions may happen
before it becomes stable again, and all of those collisions (if they happen)
must occur right to left. This is the perfect situation for

using a stack.!!!!
"""
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for item in asteroids:
            """python!!!   item < 0 < stack[-1]  """
            while stack and item < 0 < stack[-1]:
                if stack[-1] < -item:
                    stack.pop()
                    continue
                elif stack[-1] == -item:
                    stack.pop()
                break
            else:
                stack.append(item)

        return stack


#     Time Complexity: O(N)
# where NN is the number of asteroids. Our stack pushes and pops each asteroid at most once.

# Space Complexity: O(N), the size of ans.