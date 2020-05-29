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