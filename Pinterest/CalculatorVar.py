"""

第一題是給你一個string例如"2+3-999"回傳計算結果int.
    第二題加上parenthesis 例如"2+((8+2)+(3-999))"一樣回傳計算結果
    第三道题是加了变量名的。。会给你一个map比如{'a':1, 'b':2, 'c':3}，假设输入为"a+b+c+1"输出要是7，如果有未定义的变量，比如"a+b+c+1+d"输出就是7+d


224.Basic Calculator I
770. Basic Calculator IV
772. Basic Calculator III
227. Basic Calculator II

time O(N)
space O(N)

"""
##############################################
# simplest calculator without ( )
"""
(1+2-(3+4))
p
only have + -
+1+2-3-4
"""
def calculator1(s):
    total = 0
    i  = 0
    sign = 1 # +
    while i<len(s):
        c = s[i]
        if c in '+-':
            if c == '-':
                sign *=(-1)
            i+= 1
        elif c.isdigit():
            val  = ''
            while i<len(s) and s[i].isdigit():
                val += s[i]
                i+=1
            print(sign, val)
            total += sign * int(val)
            sign = 1
        else:
            #   get rid of close/open parenthesis
            i += 1
    return total
# print(calculator1('1+2-3-4+8'))

################################
"""
The expression string may contain open
( and closing parentheses ), 
the plus + or minus sign -, non-negative integers and empty spaces .

operator + - ( )
operand A,B
two stack 
p to go a single path in a while loop:
    case digits:
        calculate value and push into operand stack
    case (:
        push into operator
    case +/-:
        if operator[-1] == (
            append into operator
        else - or +:
            pop 2 oprands and 1 optors out 
            calculate value push to oprands
            push this op in 
        
if not empty
calculate all
return [-1]

"""
##################################################
def calculator2stack(s):
    if len(s)<3: return 0
    operands = []
    operator = []

    def operation():
        op = operator.pop()
        if len(operands) >= 2:
            op2 = operands.pop()
            op1 = operands.pop()
        if op == '-':
            return op1-op2
        else:
            return op1+op2

    i = 0
    while i<len(s):
        if s[i].isdigit():
            val = ''
            while s[i].isdigit():
                val += s[i]
                i += 1
            operands.append(int(val))
        elif s[i] == '(':
            operator.append(s[i])
            i+= 1
        elif s[i] in '+-':
            if operator and operator[-1] in '+-':
                operands.append(operation())
            operator.append(s[i])
            i+=1
        elif s[i] == ')':
            # calculate all operations inside ()
            while operator[-1] != '(':
                # op = operator.pop()
                # if len(operands) >= 2:
                #     op1 = operands.pop()
                #     op2 = operands.pop()
                operands.append(operation())
            operator.pop()
            i += 1
        elif s[i] == ' ':
            i+= 1
            continue
        print(operator)
        print(operands)
    # operator never have '(' -- since expression is valid always deal with ) in a single path
    while operator:
        operands.append(operation())
    return operands[-1]

# print(calculator2stack("1 +(2-3)"))
# operator
# operants 0
# op +, op2- -1 op1- 1






####################################################

"""
    2. all ()*+-/ and negative numbers
    
(1) operation func to cal
(2) priority
(3) negative 
    sign = 1
    if '-' should at beginning or after (
    sign = -1
    after val
    sign = 1
(4) (77) -> ')' will find '(' no extra modification
"""
def calculate(s: str) -> int:
    if len(s) == 1: return int(s)
    operands = []
    operator = []


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


    i = 0
    sign = 1
    while i < len(s):
        if s[i].isdigit():
            val = ''
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1
            print(val)
            operands.append(int(val)*sign)
            if sign == -1:
                sign = 1

        elif s[i] == '(':
            operator.append(s[i])
            i += 1
        elif s[i] in '+-*/':
            if s[i] == '-' and (i==0 or s[i-1] =='('):
                sign = -1
                i+= 1
                continue
            while operator and priority(operator[-1]) >= priority(s[i]):
                operands.append(operation())
            operator.append(s[i])
            i += 1
        elif s[i] == ')':
            # calculate all operations inside ()
            while operator[-1] != '(':
                operands.append(operation())
            operator.pop()
            i += 1
        elif s[i] == ' ':
            i += 1
            continue
        print(operator)
        print(operands)
    # operator never have '(' -- since expression is valid always deal with ) in a single path
    while operator:
        operands.append(operation())

    return operands[-1]

t  = "3+ (2*2 -1)"
test2 = "-1+( 2+(3-4-3)+1) - (-3 + 2)+(99)"
# print(calculate(test2))
################################################
"""
simpler approach with only - + ( ) negative
one stack
add all to total
if (
    add val of previous total to stack
    add next sign for ()
    total =0
if )
    pop sign * current total
    pop previous total
    
"""
def calsimpleone(s):
    i = 0
    total = 0
    stack = []
    sign = 1
    while i<len(s):
        if s[i].isdigit():
            val = ''
            while s[i].isdigit():
                val += s[i]
                i += 1
            total += sign*int(val)
            continue
        elif s[i] == '-':
            sign = -1
        elif s[i] == '+':
            sign = 1
        elif s[i] == '(':
            # store previous total -> 0
            stack.append(total)
            stack.append(sign)
            total = 0
            sign = 1
        elif s[i] == ')':
            total *= stack.pop()
            total += stack.pop()
        i+= 1
        # print(stack)
        # print(total, sign)

    return total
print(calsimpleone("(1-(-3+2-(8)))"))

###################################################################
"""
 3.follow up： 不光有数字和operator，还有一些变量，这些变量有些可以表示为一个数值，
    需要从给定的map里去get这个变量的value。然后有的变量不能转为数字，所以结果要包含这些
    不可变成数字的单词以及其他数字部分通过计算器得到的结果。
    
isalpha:
    if in mapping: add it to result
    else:
        add to stack and its sign "-A"
    if )
        while [-1] is str
            pop --> find out +"-A"/"+B"
        pop previous sign
        and change the sign of "xxx"
        and add total* sign + prevtotal
            
            
    

"""
def calculator_basic3_(s, mapping):
    res = [0,'']
    sign = 1
    stack = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            val = ''
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1
            res[0] += int(val) * sign
            continue
        elif s[i].isalpha():
            if s[i] in mapping:
                res[0] += mapping[s[i]] * sign
            else:
                if sign == 1:
                    res[1] += '+' + s[i]
                else:
                    res[1] += '-' + s[i]
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == '(':
            stack.append(res)
            stack.append(sign)
            res = [0,'']
        elif s[i] == ')':
            res[0] *= stack.pop()
            res[0] += stack[-1][0]
            res[1] += stack[-1][1]
            stack.pop()
        i += 1
        print(stack, res[0], res[1])
    return res






print(calculator_basic3_("1+1+a+b-(1+a)+b", {'a':2}))


