from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in range(len(T)-1,-1, -1):
            #Use 102 so min(nxt[t]) has a default value
            warmer_idx = min(nxt[t] for t in range(T[i]+1, 102))
            if warmer_idx < float('inf'):
                ans[i] = warmer_idx - i
            nxt[T[i]] = i
        return ans



Solution().dailyTemperatures([73,74,75,71,69,72,76,73])