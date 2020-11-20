RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3


def spiralPrint(matrix):
    row = len(matrix)
    col = len(matrix[0])
    remaining = row*col
    curdir = RIGHT
    curpos = (0,0)
    result = ''

    def valid(pos):
        return (0<=pos[0]<row and 0<=pos[1]<col) and not matrix[pos[0]][pos[1]]

    def nextposition(pos, direction):
        if direction==RIGHT:
            return (pos[0], pos[1]+1)
        if direction==DOWN:
            return (pos[0]+1, pos[1])
        if direction==LEFT:
            return (pos[0], pos[1]-1)
        if direction==UP:
            return (pos[0]-1, pos[1])

    def nextdirection(direction):
        if direction==DOWN:
            return LEFT
        if direction==UP:
            return RIGHT
        if direction==LEFT:
            return UP
        if direction==RIGHT:
            return DOWN

    while remaining>0:
        remaining -=1
        result += str(matrix[curpos[0]][curpos[1]])
        nextpos = nextposition(curpos, curdir)
        if not valid(nextpos):
            curdir = nextdirection(curdir)
            curpos = nextposition(curpos, curdir)
        else:
            curpos = nextposition(curpos, curdir)

    return result
