from collections import defaultdict


class Solution:
    def removeStones(self, stones) -> int:
        dic = defaultdict(list)
        # get all connected components
        for i, stone in enumerate(stones):
            for j in range(i, len(stones)):
                if stone[0] == stones[j][0] or stone[1] == stones[j][1]:
                    dic[stone].append(stones[j])
                    dic[stones[j]].append(stone)
        # dfs for each stone
        res = 0
        visited = []
        for stone in stones:
            dele = 0
            if stone not in stack:
                stack = [stone]
                visited.append(stone)
                while stack:



        def backtracking(allstone, )