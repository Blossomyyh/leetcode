from typing import List

"""
dfs 
create visited matrix to remember all the visited element in board
when we find the first character in word is (i, j) in board
    do a dfs search start (i, j)
    if i,j is current character
        if word is formed return True
    index in word move forward
    mark visited (i,j)
    go up, down, right left(check inside the border)
        for each direction we do 
            dfs(newi, newj, board, visited)
            
    :return False  
    
    
Time Complexity: {O}(N * 3 ^ L)
L
 ) where NN is the number of cells in the board and LL is the length of the word to be matched.
For the backtracking function, 
initially we could have at most 4 directions to explore, 
but further the choices are reduced into 3
 (since we won't go back to where we come from). 
 
 
 Space Complexity:O(L) 
 where LL is the length of the word to be matched
"""


class Solution:
    def dfsSearch(self, i, j, board, visited, word, wordIdx):
        if (i, j) not in visited:
            visited.append((i, j))
            if wordIdx == len(word) - 1:
                return True
        else:
            return False
        ix = [1, 0, 0, -1]
        iy = [0, 1, -1, 0]
        wordIdx += 1
        for m in range(4):
            newi = i + ix[m]
            newj = j + iy[m]
            if 0<=newi<len(board) and 0<=newj<len(board[0]) and word[wordIdx] == board[newi][newj]:
                if self.dfsSearch(newi, newj, board, visited, word, wordIdx):
                    return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = []
        wordIdx = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[wordIdx]:
                    if self.dfsSearch(i, j, board, visited, word, wordIdx):
                        return True
                    else:
                        visited = []
                        continue
        return False





    def backtracking2(self, row, col, suffix):
        # bottom case
        if len(suffix) == 0: return True
    #     check the current status before jumping into backtracking
        if row < 0 or row == self.rows or col < 0 or col == self.cols \
                or self.board[row][col] != suffix[0]:
            return False

    #     backtracking
        ret = False
        self.board[row][col] = "#"
        for rowOffset, colOffset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if self.backtracking2(row+rowOffset, col+colOffset, suffix[1:]):
                ret = True
        self.board[row][col] = suffix[0]
        return ret

    def exist2(self, board, word):
        # define global variables
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        if not word: return True
        if not board : return False
        # suppose we can modify the matrix
        for i in range(self.rows):
            for j in range(self.cols):
                if self.backtracking2(i, j, word):
                    return True
        return False




board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

# print(Solution().exist2(board, "ASFDECCB"))

"""
212. Word Search II
search several words -- Trie with { }

1. build a trie with queries
   trie is a tree to store different according to its prefix
   use dictionary to implement trie -> each node is a dictionary, 
   key - ch, value - bool to identitify whether word is end or not at this point
   tree, tea, trie
   rootNode - t - {}, false
                /   \
               r {}-false    e   {}, false 
               /\
              e   i
2. dfs the board
    for each word, do a backtracking
    o -> do a second seach, whether we search 4 directions to find the second ch 
    
"""
class WordSearch:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                #                 retrive the next node, if no , create a new one
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]
            #     normal case
            # pop out the key here --> do not need to go to this node twice
            # if Word-key is not found here, just get bool - False
            wordToMatch = currNode.pop(WORD_KEY, False)
            if wordToMatch:
                matchedWords.append(wordToMatch)
            # bottom case

            board[row][col] = '#'
            for rowOffset, colOffset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newRow = row + rowOffset
                newCol = col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                # if current node is null, just pop according key for the node
                parent.pop(letter)

        # backtracking for each letter in board
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return matchedWords


board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

# board = [["a","b"],["a","a"]]
# words = ["aaaa"]
# words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
print(WordSearch().findWords(board, words))

