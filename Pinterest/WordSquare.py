"""
425. Word Squares

b a l l
a r e a
l e a d
l a d y
"""
Input = ["area","lead","wall","lady","ball"]

"""
backtracking search
use helper functions
use prefix to generate each new word
"""
from typing import List
class solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.result = []
        self.helper([], words)
        print(self.result)

    def helper(self, curwords, words):
        if len(curwords)==len(words[0]):
            self.result.append(curwords)
            return
        nextlist = self.prefixvalid(curwords, words)
        if not nextlist:
            return
        else:
            for w in nextlist:
                self.helper(curwords+[w], words)


    def buildTrie(self, words):
        self.trie = {}
        

    def prefixvalid(self, curwords, words):
        res = []
        leng = len(curwords)
        prefix = ""
        for i in range(leng):
            prefix += curwords[i][leng]

        for w in words:
            if w.startswith(prefix):
                res.append(w)
        print(res)
        return res


solution().wordSquares(Input)







output =  [
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]


"""
make sure words can be flipped on diagonal
"""
def validWordSquare(self, words: List[str]) -> bool:




    for i in range(len(words)):
        for j in range(len(words[i])):
            if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                return False
    return True