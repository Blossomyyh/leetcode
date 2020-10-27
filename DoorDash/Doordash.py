"""
Doordash virtual onsite question:
Given a set list of pickups and deliveries for order, figure out if the given list is valid or not.
A delivery cannot happen for an order before pickup.

"""
def isValid(orders):
    if len(orders) != len(set(orders)) or len(orders)%2==1:
        return False
    pickedUp = set()
    for x in orders:
        if x[0] == 'P':
            pickedUp.add(x[1:])
        else:
            if x[1:] not in pickedUp:
                return False
            pickedUp.remove(x[1:])
    return not pickedUp


list_orders = [
    ['P1', 'P2', 'D1', 'D2'],
    ['P1', 'D1', 'P2', 'D2'],
    ['P1', 'D2', 'D1', 'P2'],
    ['P1', 'D2'],
    ['P1', 'P2'],
    ['P1', 'D1', 'D1'],
    [],
    ['P1', 'P1', 'D1'],
    ['P1', 'P1', 'D1', 'D1'],
    ['P1', 'D1', 'P1'],
    ['P1', 'D1', 'P1', 'D1']
]

for order in list_orders:
    print(order, isValid(order))


################
# DoorDash version


def validString(lists):
    stack = []
    for l in lists:
        if l[0]=='P':
            stack.append(l)
        else:
#             D
            if not stack: return False
            if stack[-1][0] == 'P':
                stack.pop()
    return True

test = ['P1','D1','P2','D2']
test = ['P1','D1','D2']
test = ['P1','P2','P3','D3', 'D2', 'D1']

print(validString(test))



# print(int("-1"))

####################
# evaluate expression

def eval(string):
    string = string.strip()
    if not string:
        print("strip")
        return 0
    expression = string.split(' ')
    if not expression: return 0
    operator = []
    operands = []

    def operation():
        op = operator.pop()
        if len(operands) >= 2:
            op2 = operands.pop()
            op1 = operands.pop()
        if op == '-':
            return op1 - op2
        elif op == '+':
            return op1 + op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return op1 // op2

    def priority(op):
        if op == '(':
            return 0
        elif op in '+-':
            return 1
        elif op in '*/':
            return 2


    for i in expression:
        if i in '*/-+':
            if not operator:
                operator.append(i)
                continue
            else:
                while operator and priority(operator[-1]) >= priority(i):
                    operands.append(operation())
                operator.append(i)
        else:
            num = int(i)
            operands.append(num)

    while operator:
        operands.append(operation())

    return operands[-1]
# string  = "1 * -2 + -3 * 4"
# string  = "1 + 135 / 134"
string  = "   "

print(eval(string))


####################
# Longest path duplicate numbers within a Matrix

"""
Given an integer matrix, find the length of the longest path that have same values. 
The matrix has no boundary limits.

From each cell, you can either move to two directions:
 horizontal or vertical. You may NOT move diagonally or move outside of the boundary.

nums = [
[1,1],
[5,5],
[5,5]
]


Thoughts
I used DFS to traverse the grid while keeping tracking of the max of longest path with same values.
This solved the problem for a boundary contrained matrix grid. 
I got rejection for it.
 I wonder if its because I couldnt solve the problem for an infinite grid,
  but for a 33 min interview i thought i did decent.
   (45mins - 15 min intro + problem solving). Is there a better alternative?
"""


"""
I recently got the same problem and coded it in a BFS manner with a visited matrix from stopping the BFS call. I think the DP solution is succinct but the time complexity is same O(rows*cols) or O(N) where N = rows * cols. Unfortunately I was rejected and I would like to know if there is a better way

Pseudo code

Initialize a visited matrix with 0's
Iterate through every cell in the input matrix and call BFS only when visited[cell] == 0
Call BFS and count and return the total number of cells visited while marking them in the visited matrix (check boundary and all cells have equal value)
Report the maximum number



Class Solution {

    public int getLargestGroup(int[][] data) {
        int rows = data.length;
        int cols = data[0].length;
        int max = -1;
        int[][] visited = new int[rows][cols];
        for(int i =0; i < rows; i++) {
            for(int j =0; j < cols; j++) {
                if (visited[i][j] == 0) {
                    int temp = findElementCount(data, visited, i,j,data[i][j]);
                    max = Math.max(temp, max);
                }
            }
        }
        return max;
    }
    
    // Actual BFS code
    private int findElementCount(int[][] data, int[][] visited, int x, int y, int element) {
        int rows = data.length;
        int cols = data[0].length;
        Queue<Pair> queue = new ArrayDeque<>();
        queue.add(new Pair(x,y));
        int count = 1;

        while (!queue.isEmpty()) {
            Pair<Integer, Integer> t = queue.poll();
            visited[t.fst][t.snd] = 1;
            for (Pair<Integer, Integer> p : getDirections(t.fst, t.snd)) {
                if (p.fst < 0 || p.fst >= rows || p.snd < 0 || p.snd >= cols || data[p.fst][p.snd] != element || visited[p.fst][p.snd] == 1) {
                    continue;
                } else {
                    queue.add(p);
                    visited[p.fst][p.snd] = 1;
                    count++;
                }
            }
        }

        return count;
    }
    
    // Directions
    private List<Pair<Integer, Integer>> getDirections(int x, int y) {
        Pair<Integer, Integer> left = new Pair<>(x, y-1);
        Pair<Integer, Integer> right = new Pair<>(x, y+1);
        Pair<Integer, Integer> up = new Pair<>(x-1, y);
        Pair<Integer, Integer> down = new Pair<>(x+1, y);

        return Arrays.asList(left, right, up, down);
    }

    // Pair class to codify a point
    public class Pair<A, B> {
        public A fst;
        public B snd;

        public Pair(A a, B b) {
            fst = a;
            snd = b;
        }
    }

"""
