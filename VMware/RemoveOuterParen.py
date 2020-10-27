"""
"(() ()) ((()))"
 121 210 123210

4 conditions:
== 0 (
==1  )
>=1  (
>1   )
"""
def removeouterpa(S):
    record = 0
    """open will define whether we are in a () or not"""
    res = ""
    for i in S:
        if i == '(' and record >= 1:
            record += 1
            res += '('
        elif i == ')' and record > 1:
            record -= 1
            res += ')'
        elif i == '(' and record == 0:
            record += 1
        elif i == ')' and record == 1:
            record -= 1
    return res
