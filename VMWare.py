from collections import defaultdict


#########################
# Usernames	System
# create	the	username portion	of	a	registration
# sys	that	requires	all	usernames	are	unique.
#  #输入 list：[bob,	alice,	bob,	alice,bob]
# 输出：[bob,alice,bob1,alice1,bob2]
def userSystem(inputList):
    dic = defaultdict(int)
    for i in range(len(inputList)):
        if inputList[i] in dic:
            dic[inputList[i]] = dic.get(inputList[i]) + 1
            inputList[i] = inputList[i] + str(dic.get(inputList[i]))
        else:
            dic[inputList[i]] = 0
    return inputList


# print(userSystem(["bob", "alice", "bob", "alice", "bob"]))

###########################
# subsequence
# 	of	a	string	is	obtained by	deleting
# zero	or	more	char	from	the	string	 while
# maintaining	order,
# \"xyz\"substring	are.
# "x"	"xy\"	\"xz\"	\"xyz\"	\"y\"	\"yz\"	\"z\"
# want	to	generate	an	array	of	all	subseq	of	a	given	string,
# omitting	the	empty	string
# IF	have	to	be	continuous,
# use	sliding	windows	two	pointer	solution
# https://leetcode.com/problems/subarray-sum-equals-k/

def buildSequences(string):
    res = [""]
    for ch in string:
        # res	+=	[r	+	char	for	 r	in	res]
        # #	this	line	is	same	as	below
        addition = []
        # for extending	substring
        for existing_str in res:
            addition.append(existing_str + ch)
        res = res + addition

    res.sort()
    res.remove("")
    return res


def buildSequence2(string):
    res = []
    for i in range(len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            res.append(string[i:j])
    return res


# print(buildSequence2("abc"))


##############################
# 3. even subarray
def evenSubarray(numbers, k):
    l = 0
    subOdd = res = 0
    for right, num in enumerate(numbers):
        # find an odd
        if num % 2 == 1:
            subOdd += 1
        if subOdd > k:
            while numbers[l] % 2 == 0:
                l += 1  # move left pointer to right until next odd
            l += 1
            subOdd -= 1
        res += right - l + 1
    return res


# print	(evenSubarray([1,2,3,3],	1))	#	6
# print	(evenSubarray([1,2,3,4],	1))	#	8
# print	(evenSubarray([1,2,3,4],	2))	#	10
# print	(evenSubarray([1,2,3,4],	3))	#	10
# print	(evenSubarray([1,2,2,3,3,4],	1))	#	2+4+6	=	12


##########################
# The	perfect	team。	 就给你一个字符串，每个 char 代表一个人擅长的科目，然后要组队，
# 要求队伍里五个人各擅长一门科目，求可以最多可以组几个队伍。数取最小
from collections import Counter

def differentTeams(skills):
    freq_table = Counter(skills)
    # ordered
    least_common_skill, least_common_count = freq_table.most_common()[-1]
    return least_common_count

##########################
# team formation ,	给个 upper	bound	和 lower	bound，
# 至少选 k 个人组队，问至少有多少 种
# 组队方式	combination	formular(C) -- different with permutation(A)
# f(x) = n!/(a!*(n-a)!)
import math

def teamFormation2( skills, k, l, r):
    def checkSkillInRange(skill):
        return l <= skills <= r

    fil = filter(checkSkillInRange, skills)
    n = len(fil)
    temp = k
    res = 0
    while temp <= n:
        res += math.factorial(n)/(math.factorial(temp) * math.factorial(n-temp))

    return res




