"""
68. Text Justification

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""
"""

"""
def fullJustify(self, words: [str], maxWidth: int) -> [str]:
    res = []
    n = len(words)
    i = 0

    while i<n:
        totalch = len(words[i])
        # try to figure out the last word of the line
        last = i+1

        # words can fit in the line
        while last<n:
            if totalch + len(words[last]) + 1>maxWidth:
                break
            totalch += 1+len(words[last])
            last += 1
        gaps = last-1 - i
        curr = []

        """ case 1 - last line / only 1  word in the line """
        if last == n or gaps == 0:
            for i in range(i, last):
                curr.append(words[i])
                curr.append(' ')
            curr = curr[:len(curr)-1] # delete last ' '
            print(curr)
            while sum(len(curr[i]) for i in range(len(curr)))<maxWidth:
                curr.append(' ')

        else:
            """ case 2: not in the last line and more than 1 word """
            space = (maxWidth - totalch)//gaps
            rest = (maxWidth- totalch)%gaps

            for idx in range(i, last-1):
                curr.append(words[idx])
                curr.append(' ')

                for j in range(0, space+1 if idx-i < rest else space):
                    curr.append(' ')
            curr.append(words[last-1])
        res.append(''.join(curr))
        i = last

    return res



