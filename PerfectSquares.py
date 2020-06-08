"""
find int  returns True if num is a perfect square else False.
cannot use sqrt
"""

def isPerfectSquare(self, num: int) -> bool:
    if num < 2:
        return True
    left, right = 2, num // 2

    while left <= right:
        x = left + (right - left) // 2
        guess_squared = x * x
        if guess_squared == num:
            return True
        elif guess_squared > num:
            right = x - 1
        else:
            left = x + 1
    return True
    # Time complexity : O(logN).

"""
Newton's Method



# Take num / 2 as a seed.

# While x * x > num, compute the next guess using Newton's method: x = (x+num//x)//2
# num//x as tangent of function f(x) = x^2-num

# Return x * x == num


"""

def isNewtonPerfectSquare(self, num: int) -> bool:
    if num < 2:
        return True
    x = num // 2
    while x * x > num:
        x = (x + num // x) // 2
    return x * x == True

# Time complexity :O(logN) because guess sequence converges quadratically.



