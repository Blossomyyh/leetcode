"""
For each digit of N, let's build the next digit of our answer ans.
 We'll find the smallest possible digit d such that ans + (d repeating) > N
 when comparing by string;
 that means d-1 must have satisfied
 ans + (d-1 repeating) <= N,
 and so we'll add d-1 to our answer.
 If we don't find such a digit, we can add a 9 instead.



"""
def monotoneIncreasingDigits(N: int) -> int:
    digits = []
    A = list(map(int, str(N)))
    for i in range(len(A)):
        for d in range(1,10):
            if digits + [d]*(len(A)-i)>A:
                digits.append(d-1)
                break
            else:
                digits.append(9)
    return int("".join(map(str, digits)))

print(monotoneIncreasingDigits(343))