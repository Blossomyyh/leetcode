"""
variable and global
"""

f =0 

def localglobal():
    global f
    f = "global"
    print(f)

localglobal()
print(f)

#del f deletes the definition that was previously declared
del f
# print(f)
# should have results like -- NameError: name 'f' is not defined
# essentially, it means you can undefine a variable in real time


"""
function & class
"""

# function is defined with 'def' keyword
# () open close parens --parenthesis
# : colon -- indicates the start of the function scope block
# python use both the scope def runner which is the colon and then indentation
# when I hit return, the next line is indended by 4 spaces (it's not limited to anything, it could be 1/2/3.. or whatever)

def func1():
    print("this function")
    # couple of things to notice here 
    # {} curly braces in java to indicate scope

print(func1())
# 1.calling functions like above line -- get "this function"
# 2.python evaluates the func1 return value to be Python constant of 'none' -- since func1 do not return a value  
print(func1) #~ bad


# arguments of function --comment out
# do not have to call the argument in particular order
def power( a, x=1):
    res = 2
    for x in range(x):
        x = x*res
    return res

# call power 1 comma 2
print(power(1,2))

# add few more lines of code down the bottom

# variable argument list -- last argument
# func has multiple arguments, it will loop over each argument and multiple them all to a running total
def multiple(*args):
    res =1
    for x in args:
        res = res * x
    return res
# try it out
print(multiple(1,2,3))


"""
conditional structures
"""
# conditionals are handled by if statement
# 2 variables and they are 10 and 100 to start with, you can see sure enough
x,y = 10, 100
# should be referenced after assignment, go ahead and fix this

# conditional flow -- if elif else
# use if-elif as a substitude for writing a switch case block.
if x < y:
    print("x<y")
elif x == y:
    print("x=y")
else:
    print("x>y")


# conditional statement -- a common else if construct all in one line
# concise way of writing the comparison logic instead of writing a more verbose if else block

st = "x>y" if x > y else "x<=y"


"""
loops
"""
# _ underscore --naming
# a stubbed out function named "main"
# a while loop execute the following lines while a particular condition evaluates true with x increments by 1
x = 0
while (x<5):
    print(x)
    x += 1

# for loop -- iterators
# % modulo -- mo
# 10 is not in the range, it prints out 5 through 9
# for loops operates over set of things, not just numbers
# for loop will iterating/looping over each element in the list, and in each iteration, x will be set to the current item that it's looking at that time
for x in range(5,10):
    if x==7: break
    # is to break the loop if the condition is met
    if (x % 2 ==0): continue
    # take x modulo / divided by 2 and if the value left over is zero, then continue
    # continue basically means skip the rest of the execution of this loop, just go back to the top of the loop and start with the next value
    print(x)
# And you can see what is happening is the break statement breaks in and causes the loop to terminate. S0, it never gets to 7 or more

day = ["Mon", "Tues", "Thurs"]
# loop with index
# enumerate would iterate over this collection like loop normally would, but in addition to return the value, it also returns the index of the item 
for i, d in enumerate(day):
    print(i, d )



"""
classes
"""
# class is a good way to encapsulating functionality that can be kept together and passed around as a complete module for use in other objects.
# I will explain it in a moment
# class is based on a superclass that I am inherited from
# functions == methods (in object-oriented projects)
# first argument of any of the methods of the class, is the self argument, which refers to the particular instance of the object itself that is been operated on.

class firstc():
    def init(self):
        print("first class")

# inherit class
class firstb(firstc):
    def init2(self):
        # first thing i will going to do is call the inherited methods on the superclass
        firstc.init(self) # invoking init class
        print("first class")
    def method(self, str):
        print(str)

# instantiate 实例化 the object instance of the class
def main():
    c = firstc()
    # call methods -- 
    c.init() # no need to care about self argument