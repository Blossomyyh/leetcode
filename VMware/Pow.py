"""
50. Pow(x, n)

# x^n --> x2 ^ n//2 ....

logn
"""
def myPow(self, x: float, n: int) -> float:
    # n negative case
    if n < 0:
        x = 1 / x
        n = -n
    # divide by n//2 make x^2
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n = n // 2
    return ans




