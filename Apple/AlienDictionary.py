"""
269. Alien Dictionary
words are sorted lexicographically by the rules of this new language. Derive the order of
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
only focus on the difference of 2 strings
"""
from collections import defaultdict
from collections import deque


def alienOrder(self, words: [str]) -> str:
    # get all orders
    order = defaultdict(set)
    indegree = defaultdict(int)
    for i in range(len(words)):
        for j in words[i]:
            order[j] = set()
            indegree[j] = 0
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        """ compare whether exist ---> word2 in word1 --> wrong """
        if len(word2) < len(word1) and word1[:len(word2)] == word2:
            return ''
        for k in range(min(len(word1), len(word2))):
            if word1[k] != word2[k]:
                # record order - children -> parent
                # make sure no duplication!!!!
                if word2[k] not in order[word1[k]]:
                    order[word1[k]].add(word2[k])
                    indegree[word2[k]] = indegree.get(word2[k]) + 1
                break
                # Check that second word isn't a prefix of first word.

    # Step 1: Find all edges and put them in reverse_adj_list.
    # print(order)
    # print(indegree)

    # use topological sort
    # traversal the graph and visited all nodes by indegree -= 1
    # have cycle?
    """ topological BFS + Queue || Indegree + Graph"""

    result = []
    queue = deque()
    for i in indegree:
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        result.append(node)
        for adj in order[node]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                queue.append(adj)

    """use length to compare cycle!! """
    if len(result) < len(indegree):
        return ""
    return ''.join(result)


"""
953. Verifying an Alien Dictionary

words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Check Adjacent Words
"""
def isAlienSorted(self, words: [str], order: str) -> bool:
    orderdic = {}
    for idx, ch in enumerate(order):
        orderdic[ch] = idx
    # compare one by one for n-1 times

    for i in range(len(words) - 1):

        word1 = words[i]
        word2 = words[i + 1]
        """ 2. same -> check length -> go next character to check"""

        if len(word1) > len(word2) and word1[:len(word2)] == word2:
            return False
        for k in range(min(len(word1), len(word2))):

            """ compare words one by one"""

            if word1[k] != word2[k]:

                """ 1. not same -> check order right -> break"""

                if orderdic[word2[k]] < orderdic[word1[k]]:
                    return False
                else:
                    """find the first difference --> break"""
                    break
    return True





