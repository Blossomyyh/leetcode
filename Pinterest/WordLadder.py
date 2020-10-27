'''127. Word Ladder'''
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
""""hit -> *it , h*t, hi*"""
"""BFS -> queue && visited"""""
# Assumptions
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
from collections import defaultdict
from collections import deque

"""
Assumption: wordlist is valid with all same length word

\\1. build a dictionary to find adjacent word for wordList
    key (intermediate production) *it , h*t..
    values list of words which satisfy the key's format
\\2. use BFS to start from beginWord 
    visited set()
    queue append (first word, [beginword])
    while loop where queue not empty
         got the current node and list
         search in the dictionary we build and traversal those values
            if we  find the endword
                break
            else if not visited
                append to the queue - (word, list + [word])
                continue
                
\\ Time complexity : O(M ^2 × N), 
        where M is the length of each word 
        -- each time we go through the ch and 
        --- \\ build a new string M, M times for 1 word
        N is the total number of words in the input word list.
        
\\ Space complexity: O(M^2 ×N).
    Each word in the word list would have M intermediate combinations-M length  - n word
    
    Queue for BFS in worst case would need a space for all O(N) words and 
    this would also result in a space complexity of O(M \times N)O(M×N).
                
"""

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


from collections import defaultdict
from collections import deque
def wordShortestPathDIC( beginWord, endWord, wordList) -> int:
    if not wordList: return []
    wordDic = defaultdict(list)
    listOfword = set()
#     build the dictionary
    for word in wordList:
        for i in range(len(word)):
            wordformat = word[:i]+ "*" + word[i+1:]
            wordDic[wordformat].append(word)
    print(wordDic)

    '''
    def all_possible_values(word, bank):
        all_values = []
        for i in range(len(word)):
            for char in {"A", "C", "G", "T"}:
                mutate = word[:i] + char + word[i + 1:]
                # check if the new mutation is valid ie in the bank
                if mutate in bank:
                    all_values.append(mutate)
                    bank.remove(mutate)
        return all_values
    '''

#     BFS to find the first occurrence of endword
    queue = deque()
    queue.append((beginWord, [beginWord]))
    visited = set()
    while queue:
        node, curList = queue.popleft()
        listOfword.add(node)
        for i in range(len(node)):
            wordformat = node[:i]+"*"+node[i+1:]
            for nextWord in wordDic[wordformat]:
                if nextWord == endWord:
                    return curList + [endWord], len(curList)+1
                else:
                    if nextWord not in listOfword:
                        queue.append((nextWord, curList + [nextWord]))
                        # or level += 1

    return []
print(wordShortestPathDIC(beginWord, endWord, wordList))



######################################
# Similar question

'''
433. Minimum Genetic Mutation

\\ shall use  \\curlevel\\ or \\curnode \\   !!!!!!!!!!!!\\

'''


from collections import deque

from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank: return -1
        visited = set()
        #         BFS
        queue = deque()

        def findnextgene(node):
            nextlist = set()
            for i in range(len(node)):
                for ch in ["A", "C", "G", "T"]:
                    newword = node[:i] + ch + node[i + 1:]
                    if newword not in nextlist and newword in bank:
                        nextlist.add(newword)
            print(nextlist)
            return list(nextlist)

        level = 0
        queue.append((start, level))
        while queue:
            node, curlevel = queue.popleft()
            visited.add(node)
            for adj in findnextgene(node):

                if adj == end:
                    return curlevel + 1
                else:
                    if adj not in visited:
                        queue.append((adj, curlevel + 1))
        return -1
















