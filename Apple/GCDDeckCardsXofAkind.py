"""
914. X of a Kind in a Deck of Cards

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
"""

"""
Greatest common divisor

Euclid's Algorithm
1. Given two whole numbers, subtract the smaller number from the larger number and note the result.
2. Repeat the process subtracting the smaller number from the result 
   until the result is smaller than the original small number.
3. Use the original small number as the new larger number. 
4. Subtract the result from Step 2 from the new larger number.
5. Repeat the process for every new larger number and smaller number until you reach zero.
6. When you reach zero, go back one calculation: the GCF is the number you found just before the zero result.

"""
from collections import Counter
def hasGroupsSizeX(self, deck: [int]) -> bool:
    def gcd(a, b):

        while b:
            a, b = b, a % b
        return a

    """
    Euclid's algorithm:
        a % b --> get remaining of a --> gcd must within the range
    """
    count = Counter(deck)
    freqs = count.values()
    div = freqs[0]
    for i in freqs[1:]:
        div = gcd(div, i)

    return div >= 2



"""
Time Complexity: O(N log^2 N) 
    where NN is the number of votes. 
    If there are C_iC cards with number ii, 
    then each gcd operation is naively O(log^2 C_i)
    Better bounds exist, 
Space Complexity: O(N).
"""

print(3%10)