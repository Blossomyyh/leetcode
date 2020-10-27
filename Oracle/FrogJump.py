"""
403. Frog Jump

"""
def canCross(self, stones) -> bool:
    # store index i can reach

    jump = dict((x, set()) for x in stones)
    # create a dictionary where the keys are the stones
    # and the values are empty sets that will contain
    # integers which represent the jump lengths that
    # can reach the stone represented by the key
    jump = {0:[1]}

    # catches a tricky test case: stones = [0,2]
    if stones[1] != 1:
        return False

    for i in range(len(stones[1:])):
        # iterate over each jump length used to reach
        # the current stone
        for j in jump[stones[i]]:
            # can jump 3
            for k in [j-1, j, j+1]:
                if k>0 and stones[i]+k in jump:
                    # add that jump length used to get there to
                    # the set of jump lengths for the stone the
                    # jump puts the frog on
                    jump[stones[i]+k].add(k)
    return jump[stones[-1]] != set()

