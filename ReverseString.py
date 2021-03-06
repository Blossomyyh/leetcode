def reverseStr(self, s: str, k: int) -> str:
    a = list(s)
    for i in range(0, len(a), 2*k):
        a[i:i+k] = reversed(a[i:i+k])
    return "".join(a)
            
            
# Instead of using the reversed() function.It is better to reverse using slicing
# a[i:i+k] = a[i:i+k][::-1]
# a[i:i+k] = reversed(a[i:i+k]

"""todo: slice notation in """
""" python ---- list[<start>:<stop>:<step>] """

# So, when you do a[::-1], it starts from the end towards the first taking each element. 
# So it reverses a. This is applicable for lists/tuples as well

# >>> a = '1234'
# >>> a[::-1]
# '4321'
# a = '1234'
# print a[::2]
# -- 13
# a = '1234'
# print a[3:0:-1]
# -- 432


"""loop to reverse"""
str = "Python" # initial string
reversedString=[]
index = len(str) # calculate length of string and save in index
while index > 0:
    reversedString += str[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(reversedString) # reversed string

"""join to reverse"""
print("".join(reversed(str)))


import sys
import re
text = "".join(sys.stdin.readlines())
# print(text)
name = re.split(' |,',text)
# print(name)
print(name[-1],  "".join(reversed(name[0])))