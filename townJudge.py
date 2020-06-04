from typing import List


class Solution:
    """
    town judge 
    form a graph
    with two arrays
    """
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        #The town judge has an outdegree of 0 and an indegree of N - 1 
        #because they trust nobody, and everybody trusts them (except themselves).
        
        # trust.length < N - 1, then we can immediately return -1.
        if len(trust) < N-1: return -1;
        
        indegree = [0]* (N+1)
        outdegree = [0] * (N+1)
        
        for a,b in trust:
            outdegree[a] +=1
            indegree[b] +=1
        for i in range(1, N+1):
            if indegree[i]==N-1 and outdegree[i]==0:
                return i
        return -1
        
        # Time Complexity : O(E+N) edges because E>N then O(E)
        # Space Complexity : O(N)