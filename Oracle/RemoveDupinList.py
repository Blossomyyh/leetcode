"""

Memoise Count
Initialize counts array of size n.

Iterate through the string:

If the current character is the same as the one before, set counts[i] to counts[i - 1] + 1.

Otherwise, set counts[i] to 1.
If counts[i] equals k, erase last k characters and decrease i by k.


Stack with Reconstruction

Iterate through the string:
If the current character is the same as on the top of the stack, increment the count.

Otherwise, push 1 and the current character to the stack.
If the count on the top of the stack equals k, pop from the stack.

Build the result string using characters and counts in the stack.


"""


def removeDuplicates(self, s: str, k: int) -> str:
    stack = [['#', 0]]
    # stack to pop , stark with '#'--> f==0 so no worry for last step
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] >= k:
                stack.pop()
        else:
            stack.append([c, 1])
            #join to reconstract
    return "".join(c * f for c, f, in stack)