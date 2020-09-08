"""
227. Basic Calculator II

he expression string contains only non-negative integers,
 +, -, *, / operators and empty spaces .
 The integer division should truncate toward zero.
"""
import math




"""
with 2 stack
while operation 
"""
def getNumber(ele, s):
    num = 0
    while ele < len(s) and s[ele].isdigit() :
        num = num*10 + int(s[ele])
        ele += 1
    return num, ele


def compare(op1, op2):
    if op1 == op2:
        return 0
    elif (op1 == '*' or op1 == '/') and (op2== '+' or op2 == '-'):
        return 1
    elif  (op1== '+' or op1 == '-') and (op2 == '*' or op2 == '/'):
        return -1
def operation(oprand1, oprand2, op):
    val = 0
    if op == '+':
        return oprand1 + oprand2
    elif op =='-':
        return oprand1 - oprand2
    elif op == '*':
        return oprand1 * oprand2
    elif op == '/':
        return math.trunc(oprand1/oprand2)

def simpleCalculator2(s: str) -> int:
    opSet = {'*', '/', '+', '-'}
    numStack, opStack = [], []
    ele = 0
    while ele < len(s):
        if s[ele].isdigit():
            num, ele = getNumber(ele, s)
        elif s[ele] in opSet:
            if compare(s[ele], opStack[-1]) ==1:
                opStack.append(s[ele])
            else:
                while compare(s[ele], opStack[-1]) !=1:
                    curOp = opStack.pop()
                    oprand1 = numStack.pop()
                    oprand2 = numStack.pop()
                    numStack.append(operation(oprand1, oprand2, curOp))
                opStack.append(s[ele])
            ele += 1

simpleCalculator2("3+2*2")











class Solution:
    def calculate(self, s: str) -> int:
        ## RC ##
        ## APPROACH : 2 STACKS ##
        ## Similar to Leetcode: 772. Basic Calculator ##
        ## Similar to Leetcode: 224. Basic Calculator ##

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        def operation(op, second, first):
            if op == "+":
                return first + second
            elif op == "-":
                return first - second
            elif op == "*":
                return first * second
            elif op == "/":  # integer division
                return first // second

        def precedence(current_op, op_from_ops):
            if (op_from_ops == "(" or op_from_ops == ")"):
                return False
            if (current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
                return False
            return True  # when curr = "+", top of ops = "*" or "/"

        if not s: return 0
        N = len(s)
        nums = [] if (s[0] != '-') else [0]  # edge case -1 + 2/3
        ops = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = c
                while i < N - 1 and s[i + 1].isdigit():  # more than 1 digit numbers
                    num += s[i + 1]
                    i += 1
                nums.append(int(num))
            elif c == "(":
                ops.append(c)
                if (i + 1 < N and s[i + 1] == '-'):
                    nums.append(0)  # "1 - (-7)" edge case.
            elif c == ")":
                while ops[-1] != "(":  # do the math when we encounter a ')' until '('
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()  # watch out, popping open brace '('
            elif c in ["+", "-", "*", "/"]:
                while len(ops) != 0 and precedence(c, ops[
                    -1]):  # check for precedence order and make calculations, APPEND RESULT TO NUMS STACK EVERY TIME.
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.append(c)  # append to operators stack
            i += 1  # basic while loop increment

        while len(ops) > 0:  # finally we perform calculations till stack is empty.
            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))

        return nums.pop()


"""tricky python calculation"""
def calculate(self, s: str) -> int:
    num = 0
    res = 0
    pre_op = '+'
    s += '+'
    stack = []
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == ' ':
            pass
        else:
            if pre_op == '+':
                stack.append(num)
            elif pre_op == '-':
                stack.append(-num)
            elif pre_op == '*':
                operant = stack.pop()
                stack.append((operant * num))
            elif pre_op == '/':
                operant = stack.pop()
                stack.append(math.trunc(operant / num))
            num = 0
            pre_op = c
    return sum(stack)



