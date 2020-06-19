def monotoneIncreasingDigits(N: int) -> int:
    digits = []
    A = map(int, str(N))
    for i in A:
        for d in range(1,10):
            if digits + [d]*(len(A)-i)>A:
                digits.append(d)
                break
            else:
                digits.append(9)
    return int("".join(map(str, digits)))


monotoneIncreasingDigits(343)