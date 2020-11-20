"""
Given an array of integers and some value X, print the pairs of integers that sum to X
example: {​​​​​5, 1, 2, 3, 4, 6, -1, 0, 9}​​​​​   X = 5
Answer = (2, 3)  (1, 4), (6, -1), (5, 0)
dictionary {5:1 1:1}
target -i

Unitcase
    positive / negative

Integration test ->
Security test -- XXS, SQL, abuse

string localization

Performance -> time case --> calculate time with 10, 1000, 10000 to see the time increase figure
Update test 升级


"""
def getPair(nums, target):
    if not nums or len(nums)<2:
        print("Nums not valid")
        return

    dictionary = set()
    result = set()
    # traversal the nums
    for i in nums:
        if target - i in dictionary:
            result.add((target-i, i))
        dictionary.add(i)

    # print result
    if len(result) == 0:
        print("No case found !")
    else:
        for item in result:
            print("(" + str(item[0]) + ", " + str(item[1]) + ")")
    return


nums = [5, 1, 2, 2, 3, 4, 6, -1, 0, 9]
# nums = [5, 5, 5]
target = -2
getPair(nums, target)