# if need to 0.001 -> turn range to (0- x*10**3//2)

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot

        return right

    def sqrt(self, x, precision):
        """find nearest integer first"""
        start, end = 0,x
        ans = 1
        while start<=end:
            mid = (start+end)//2
            if mid*mid<x:
                start = mid + 1
            elif mid*mid>x:
                end = mid - 1
            else:
                ans = mid
                break

        # For computing the fractional part
        # of square root upto given precision
        increment = 0.1
        for i in range(precision):
            while ans*ans<x:
                ans += increment
            ans -= increment
            increment = increment / 10
            print(ans)
        return round(ans, precision)


""""""


# Function to find square root of
# given number upto given precision
def squareRoot(number, precision):
    start = 0
    end, ans = number, 1

    # For computing integral part
    # of square root of number
    while (start <= end):
        mid = int((start + end) / 2)

        if (mid * mid == number):
            ans = mid
            break

        # incrementing start if integral
        # part lies on right side of the mid
        if (mid * mid < number):
            start = mid + 1


        # decrementing end if integral part
        # lies on the left side of the mid
        else:
            end = mid - 1

    # For computing the fractional part
    # of square root upto given precision
    increment = 0.1
    for i in range(0, precision):
        while (ans * ans <= number):
            ans += increment

            # loop terminates when ans * ans > number
        ans = ans - increment
        increment = increment / 10

    return ans


# Driver code
print(round(squareRoot(50, 3), 4))
print(round(squareRoot(10, 4), 4))
print(Solution().sqrt(50,3))
print(Solution().sqrt(10,4))
