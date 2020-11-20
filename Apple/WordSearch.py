from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                #                 retrive the next node, if no , create a new one
                # node = node.setdefault(letter, {})
                if letter not in node:
                    node[letter] =  {}
                node = node[letter]
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]
            #     normal case
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
                parent.pop(letter)

        # backtracking for each letter in board
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return matchedWords