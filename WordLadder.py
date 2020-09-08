# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

""""hit -> *it , h*t, hi*"""
"""BFS -> queue && visited"""""


# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
from collections import defaultdict
from collections import deque
class solution:
    def wordShortestPath(self, beginWord, endWord, wordList) -> int:
        # wipe out edge cases
        #         have same length

        l = len(beginWord)
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        # init dict for wordlist
        dic = defaultdict(list)
        # preprocess wordlist
        for word in wordList:
            for i in l:
                intermediate = word[:i] + "*" + word[i+1:]
                dic[intermediate].append(word)

        # BFS
                # here we got tree for search:   queue for BFS
        # store current word and the steps went through --> tuple
        queue = deque()
        queue.append((beginWord, 1))

        # init visited dict
        visited = set(beginWord)

        while queue:
            curword, level = queue.popleft()
            for i in range(l):
                inter =  word[:i] + "*" + word[i+1:]
                for word in dic:
                    if word == endWord: return level +1
                    if word not in visited:
                        queue.append((word, level +1))
                        visited.append(word)
                """decrease space complexity"""
                dic[inter] = []
        return 0


