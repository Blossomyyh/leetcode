"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

"""
# Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]

"""

start from begin word -- first node "hit" -- level 0
    add all last level into queue
    BFS building next level 
    queue pop
        store all next level word in curlevel, all according list
        if == endword:
            return the list contain endword in the level

"""
import collections
def findAllLadders(beginWord, endWord, wordList):

    # Time complexity for word -- L*L*26
    def findall(word):
        res = set()
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                newword = word[:i]+ch+word[i+1:]
                if newword in wordList and newword not in res:
                    res.add(newword)
        print(res)
        return list(res)
    # sometimes, key has different towards it so [[]]
    eachLevel = {beginWord: [[beginWord]]}
    # make a set for all word and remove from it
    # since still need shortest path
    notvisited = set(wordList)
    while eachLevel:
        nextLevel = {}
        for word in eachLevel:
            if word == endWord:
                return eachLevel[word]
            for adj in findall(word):
                if adj in notvisited:
                    if adj not in nextLevel:
                        nextLevel[adj] = []
                    for path in eachLevel[word]:
                        nextLevel[adj].append(path + [adj])
        print(nextLevel)
        notvisited -= set(nextLevel.keys())
        eachLevel = nextLevel

    return []
print(findAllLadders(beginWord, endWord, wordList))



class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res

print(Solution().findLadders(beginWord, endWord, wordList))

'''
0. {'hit': [['hit']]}
1. {'hot': [['hit', 'hot']]})
2. {'dot': [['hit', 'hot', 'dot']], 'lot': [['hit', 'hot', 'lot']]})
3. {'dog': [['hit', 'hot', 'dot', 'dog']], 'log': [['hit', 'hot', 'lot', 'log']]})
4. {'cog': [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]})

'''