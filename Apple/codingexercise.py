"""
On a 4x4 board, find words that can be formed by a sequence of adjacent (top, bottom, left, right, diagonal) letters.
Words must be 3 or more letters.
You may move to any of 8 adjacent letters, however,
a word should not have multiple instances of the same cell.

*Your solution should accept any board layout of letters.
To check if a string is a valid word you may implement a naive dictionary solution for simplicity.

----------------------------------
Input: the board and words list
Output: list of words in the board
* L is length of word
* N is number of words
* M is number of cells in board

Solution:
1. Build Dictionary - use Trie structure
    Time Complexity: O(NL)
    Space Complexity:  O(NL)

2. Search Words in Board - use BFS
    Time Complexity: O(M * 8*7^(L-1))
    Space Complexity:  O(N)


Optimization:
1. pruning trie !
2. modify board -># rather than set
"""
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = ""

class WordSearch:
    def __init__(self, board):
        self.board = board
        self.row = len(board)
        self.col = len(board[0])
        # use set to store results
        self.result = set()
        # use TrieNode to build dictionary
        self.root = TrieNode()

    def buildDictionary(self, words):
        for word in words:
            node = self.root
            for character in word:
                node = node.children[character]
            node.word = word

    def checkValid(self, i, j):
        return 0<= i <self.row and 0<= j < self.col

    def backtracking(self, i, j, currSet, currNode):
        # bottom case
        if currNode.word:
            self.result.add(currNode.word)

        # search 8 directions
        for ix, jx in [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1),(-1, -1)]:
            if self.checkValid(i+ix, j+jx):
                character = self.board[i+ix][j+jx]
                # if character in next node, do backtracking again
                if character in currNode.children:
                    currSet.add((i+ix, j+jx))
                    self.backtracking(i+ix, j+jx, currSet, currNode.children[character])
                    currSet.remove((i + ix, j + jx))

    def searchBoard(self):
        # use BFS to traversal the tree and find words
        for i in range(self.row):
            for j in range(self.col):
                self.backtracking(i, j, set(), self.root)
        return self.result

if __name__ == "__main__":
    board = [
        ['R', 'A', 'E', 'L'],
        ['M', 'O', 'F', 'S'],
        ['T', 'E', 'O', 'K'],
        ['N', 'A', 'T', 'I']
    ]
    words = ["FOOT", "LEAF", "ROOF", "ROOT", "LEAR", "TEA", "MEAT", "MET", "MEAN", "SEA"]
    wordsearch = WordSearch(board)
    wordsearch.buildDictionary(words)
    print(wordsearch.searchBoard())
    # {'MEAT', 'ROOT', 'TEA', 'LEAF', 'ROOF', 'MET', 'LEAR', 'FOOT', 'MEAN', 'SEA'}

