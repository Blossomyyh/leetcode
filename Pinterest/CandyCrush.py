"""
crush the duplicate candy - 3



"""
"""
One line crush
比如输入是 CABBBAAD
第一步消掉BBB -> CAAAD
第二步消掉AAA -> CD
"""

def candycrush(candies):
    stack = []
    for candy in candies:
        if len(stack)>=2:
            if stack[-1]==stack[-2]==candy:
                stack.pop()
                stack.pop()
                continue
            else:
                stack.append(candy)
        elif len(stack)<2:
            stack.append(candy)
    return "".join(stack)
print(candycrush("122344555433211222666ss"))
"""

Input:
board =
[[110,5,112,113,114],
 [210,211,5,213,214],
 [310,311,3,313,314],
 [410,411,412,5,414],
 [5,  1,  512, 3,3],
 [610,4, 1, 613,614],
 [710,1, 2, 713,714],
 [810,1, 2, 1,  1],
 [1,   1,2,  2, 2],
 [4,  1, 4,  4,1014]]
If three or more candies of the same type are adjacent vertically or horizontally, 
"crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board 
has candies on top of itself, then these candies will drop until 
they hit a candy or bottom at the same time. 
(No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed.
 If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), 
then return the current board.
Output:
[[0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [110,0,0,0,114],
 [210,0,0,0,214],
 [310,0,0,113,314],
 [410,0,0,213,414],
 [610,211,112,313,614],
 [710,311,412,613,714],
 [810,411,512,713,1014]]
"""
"""
sliding window for column and row seperately
each time we crush the candies and create a new matrix :
    do sliding window for each row and column:
        window size as 3 (2 pointers)
        mark as 0 
    update the matrix
"""
