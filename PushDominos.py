class Solution:
    """
    push dominos : some of them will collapse/ stay still
    we can encode it as ...RL...
    we can apply a greedy approach
    go through left to right and calculate all the right forces & right to left to calculate all the left forces.
    example: 0 0 10 9 8 7
    encounter a large force we can use 10, each second the power will decrease by 1
    basically that represents the right pushing power we had overtime
    if we see a left force, we just set it to 0
    cause it just negates all the right power we have, we lose our right power
    Then we go reverse order from right to left, and we do negative this time, the same applies to left force.

    after recording l/r power, we can sum it up
    positive - right ; negative - left; 0 - stand still

    """

    def pushDominoes(self, dominoes: str) -> str:
        forces = [0] * len(dominoes)
        maxForce = len(dominoes)
        # right
        force = 0
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                force = maxForce
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(0, force-1)
            forces[i] = force
        # left
        force = 0
        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] == 'R':
                force = 0
            elif dominoes[i] == 'L':
                force = maxForce
            else:
                force = max(0, force -1)
            forces[i] -= force

        result = ''
        """string do not support assignment!! need to create a new one!!"""
        for i in range(len(dominoes)):
            if forces[i] < 0:
                result += 'L'
            elif forces[i] == 0:
                result += '.'
            elif forces[i] > 0 :
                result += 'R'
        return result

    """
    Sliding window solution:'
    
    
    If we have say "A....B",
     where A = B, then we should write "AAAAAA".
    
    If we have "R....L", 
    then we will write "RRRLLL", or "RRR.LLL" if we have an odd number of dots. If the initial symbols are at positions i and j, we can check our distance k-i and j-k to decide at position k whether to write 'L', 'R', or '.'.
    
    (If we have "L....R" we don't do anything. 
    We can skip this case.)
    
     'R......R' => 'RRRRRRR'
     'R......L' => 'RRRRLLLL' or 'RRR.LLL'
    'L......R' => 'L.....R'
      'L......L' => 'LLLLLLLL'
    
    """
    def pushDominoes2(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        ans = list(dominoes)

        for (i,x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            #     only consider x=R and y=L
            elif x > y:
                for k in range(i+1, j):
                    if k-i > j-k:
                        ans[k] = 'L'
                    elif k-i < j-k:
                        ans[k] = 'R'
                    else:
                        ans[k] = '.'

        return "".join(ans)




print(Solution().pushDominoes2('..R...L..R.'))


def pushDominoes3(dominoes):
    """
    :type dominoes: str
    :rtype: str
    """
    while True:
        # mock the situation of each second
        # first detect whether we have 'R.L' --> hide it and then tackle .L and R.
        # finally replace | with R.L
        new_dominoes = dominoes.replace('R.L', '|').replace('.L', 'LL').replace('R.', 'RR').replace('|', 'R.L')
        # whether it will not change any more
        if new_dominoes == dominoes:
            break
        else:
            dominoes = new_dominoes

    return dominoes

print(pushDominoes3('..R...L..R.'))