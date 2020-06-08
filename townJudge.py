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
        if len(trust) < N-1 : return -1;
        
        indegree = [0] * (N+1)
        outdegree = [0] * (N+1)
        
        for a,b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        for i in range(1, N+1):
            if indegree[i] == N-1 and outdegree[i]==0:
                return i
        return -1
        
        # Time Complexity : O(E+N) edges because E>N then O(E)
        # Space Complexity : O(N)

    def findOneJudge(self, N: int, trust: List[List[int]]) -> int:
        # The town judge has an outdegree of 0 and an indegree of N - 1
        # because they trust nobody, and everybody trusts them (except themselves).

        # trust.length < N - 1, then we can immediately return -1.
        if len(trust) < N - 1: return -1;

        degree = [0] * (N + 1)  # indegree - outdegreee

        for a, b in trust:
            degree[a] -= 1
            degree[b] += 1
        for i in range(1, N + 1):
            if degree[i] == N - 1:
                return i
        # for i, score in enumerate(degree[1:], 1):
        # if score==N-1:
        # return i
        return -1

        # Time Complexity : O(E+N) edges because E>N then O(E)
        # Space Complexity : O(N)

    """
    If there were two town judges, then they would have to trust each other, 
    otherwise we'd have a town judge not trusted by everybody. 
    But this doesn't work, because town judges aren't supposed to trust anybody. 
    Therefore, we know there can be at most one town judge.
    """