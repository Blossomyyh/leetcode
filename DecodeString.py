"""
394. Decode String

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
 s = "3[a2[c]]"
 "accaccacc"
"""
s = "3[a]2[bc]"
s = "asd3[a2[c]]"

"""
\\ sol1 stack
append digit cha [ in stack
when ] pop out cha repeat with number
"""


def decodestring(s):
    stack = []
    number = 0
    curstr = ""

    for i in s:
        if i.isdigit():
            number = int(i)
        elif i.isalpha():
            curstr += i
        elif i == '[':
            stack.append(curstr)
            stack.append(number)
            curstr = ""
            number = 0
        elif i == ']':
            number = stack.pop()
            prevstr = stack.pop()
            curstr = prevstr + number* curstr
    return curstr
print(decodestring(s))

"""
\\ sol2: recursion

"""
class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def helper():
            multi = 0
            sub = []
            while self.i < len(s):
                char = s[self.i]
                self.i += 1

                if char.isdigit():
                    multi = multi * 10 + int(char)

                elif char == '[':
                    sub += multi * helper()
                    multi = 0

                elif char == ']':
                    return sub

                else:
                    sub.append(char)

            return "".join(sub)

        return helper()


""""""


