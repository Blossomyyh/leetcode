def removeKdigits(num: str, k: int) -> str :
    """
    :type num: str
    :type k: int
    :rtype: str
    """

    # 1). for each digit, if the digit is less than the top of the stack, i.e.
    # the left neighbor of the digit, then we pop the stack, i.e. removing the left neighbor.
    #  At the end, we push the digit to the stack.

    # 2). we repeat the above step (1) until any of the conditions does not hold any more,
    # e.g. the stack is empty (no more digits left). or in another case, we have already removed k digits,
    # therefore mission accomplished.

    stack = []
    for n in num:
        while stack and k and stack[-1] > n:
            stack.pop()
            k -= 1
        stack.append(n)
    # - Trunk the remaining K digits at the end
    # - in the case k==0: return the entire list
    res = stack[:-k] if k else stack
    # if k != 0 then we get stack from [0, -k] or else we have whole stack as result

    """lstrip()"""
    # removes any leading characters (space is the default leading character to remove)
    """join()"""
    # Join all items in a tuple into a string, using "" as separator
    # if we got "" then return "0" instead
    return "".join(res).lstrip('0') or "0"
