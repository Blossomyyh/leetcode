import collections

# There are N students in a class.
# Some of them are friends, while some are not.
# Their friendship is transitive in nature.
# For example, if A is a direct friend of B, and B is a direct friend of C,
# then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between students in the class.
# If M[i][j] = 1, then the ith and jth students are direct friends with each other,
#  otherwise not. And you have to output the total number of friend circles among all the students.
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.

"""
Depth First Search


go through all unvisited people(1) from 1 to n-1 (row)
    check all element in its column 1-n-1
    if 1 :
        mark x,y and y,x visited -> #
        do dfs for this node:
            go to the column of this node
            check whether a 1:
                do dfs to the current node recursively
    find a circle output+ 1
return output
"""
from typing import List


class Solution:
    def findCircleNumDFS(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        if len(M) == 1:
            return 1
        output = 0

        def dfs(i):
            for j in range(len(M)):
                if M[i][j] == 1:
                    M[i][j] = M[j][i] = -1
                    dfs(j)
                    M[i][j] = M[j][i] = 1

        for i in range(len(M)):
            if M[i][i] == 1:
                dfs(i)
                output += 1

        return output


M = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]
print(Solution().findCircleNumDFS(M))

"""
Breadth First Search

go throught all the people and add it to the queue
while deque:
    popleft to get the current person and visit this person (mark it -1)
    for j from 0 to col:
        if 1:
            queue.append this person
            

"""


def findCircleNummyBFS(M: List[List[int]]) -> int:
    if not M:
        return 0
    if len(M) == 1:
        return 1
    # turn the adj matrix to Adj list
    friend = collections.defaultdict(set)
    for i in range(len(M)):
        for j in range(i + 1, len(M[0])):
            if M[i][j] == 1:
                friend[i].add(j)
                friend[j].add(i)

    output, circles, seen = 0, [], set()
    print(friend)

    def bfs(queue, oneCircle):
        seen.add(queue[0])
        for person in queue:
            oneCircle.add(person)
            for j in friend[person]:
                if j not in seen:
                    seen.add(j)
                    queue.append(j)
        return oneCircle

    for f in range(len(M)):
        if f not in seen:
            circles.append(bfs([f], set()))
    print(circles)
    return len(circles)


# DFS & BFS
def findCircleNumBFS(M: List[List[int]]) -> int:
    friend = collections.defaultdict(set)
    seen, circles, n = set(), [], len(M)
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j]:
                friend[i].add(j)
                friend[j].add(i)
    print(friend)

    # def dfs(person, circle):  # you can also call it backtrack
    #     nonlocal seen
    #     seen.add(person)
    #     circle.add(person)
    #     for j in friend[person]:
    #         if j not in seen:
    #             dfs(j, circle)
    #     return circle
    #
    # for person in range(n):
    #     if person not in seen:
    #         circles.append(dfs(person, set()))
    # print(circles)
    # return len(circles)

    def BFS(queue, circle):
        seen.add(queue[0])
        for person in queue:
            circle.add(person)
            for j in friend[person]:
                if j not in seen:
                    seen.add(j)
                    queue.append(j)  # Python list append is time consuming, so recursion DFS is better in time.
        return circle

    for person in range(n):
        if person not in seen:
            # if not visited before, create a new queue for another circle and traverse this one BFS
            circles.append(BFS([person], set()))
    print(circles)
    return len(circles)


print(findCircleNummyBFS(M))

"""
Union Find

can do on both adj list and adj matrix
no need to turn matrix to list
 
    pseudo code:
        1. find parent function -- find the parent of a single node(assume that parent is the node itself at first)
        
        2. union function -- simply union the x to be the parent of y
        
        \\ a list to store all the parent node for each person
         go through the friend of each person -> turn the person as parent node of the friend
         find and union
         return number of root parent node
        
"""


def unionFindFriendCircle(M: List[List[int]]) -> int:
    if not M:
        return 0
    if len(M) == 1:
        return 1
    unionTree = [i for i in range(len(M))]

    def find(person):
        if unionTree[person] == person:
            return unionTree[person]
        else:
            unionTree[person] = find(unionTree[person])

    def union(personx, persony):
        unionTree[find(personx)] = find(persony)

    #  go through half of the matrix
    for i in range(len(M)):
        for j in range(i + 1, len(M)):
            if M[i][j] == 1:
                union(i, j)
    print(unionTree)

    for i in range(len(unionTree)):
        unionTree[i] = find(unionTree[i])

    print(unionTree)
    return len(set(unionTree))


print(unionFindFriendCircle(M))

#####################################
"""
\\ friend cicle

1. print out friends of each person

-go through s1 to get info of each employ
-go through s2 to add friends for x,y separatly in a list

"""

s1 = [
    "1,Richard,Engineering",
    "2,Erlich,HR",
    "3,Monica,Business",
    "4,Dinesh,Engineering",
    "6,Carla,Engineering",
    "9,Laurie,Directors"
]
s2 = [
    "1,2",
    "1,3",
    "1,6",
    "2,4"
]

from collections import defaultdict


def friendCycle1(employee_info, friend_relation):
    friend = defaultdict(set)
    for info in employee_info:
        num = info.split(',')[0]
        friend[num] = set()
    for relation in friend_relation:
        """ you can do x,y = ..split()  to get the value"""
        x, y = relation.split(',')
        friend[x].add(y)
        friend[y].add(x)
    print(friend)

    for person, friends in friend.items():
        """use join to print out a list !!!!"""
        print(person, ':', " ".join(friends))

friendCycle1(s1, s2)

"""
2. for each department , count the number of person and how many people has friends not in this department

build dictionary for employee --> department
build another one for department --> [person]
build another one for department --> [numofperson, numofdistrict]
"""

def friendCycle2(employee_info, friend_relation):
    friend = defaultdict(set)
    for relation in friend_relation:
        """ you can do x,y = ..split()  to get the value"""
        x, y = relation.split(',')
        friend[x].add(y)
        friend[y].add(x)
    print(friend)

    employDepart = defaultdict(str)
    for info in employee_info:
        num,_,department = info.split(',')
        employDepart[num] = department

    print(employDepart)

    departmentDic = defaultdict(set)
    for num in employDepart:
        department = employDepart[num]
        departmentDic[department].add(num)
    print(departmentDic)

    result = defaultdict(list)
    for key, employees in departmentDic.items():
        num = len(employees)
        district = 0

        for employ in list(employees):
            """  !!!!!!!!  careful about naminng !!!!!!!!"""
            for friends in friend[employ]:
                if employDepart[friends] != key:
                    district = 1
                    break
        result[key] = [num, district]
    return result

print(friendCycle2(s1, s2))




"""
3. find out whether those person are all connected with each other

dfs traverse all inn friend dcitionary
for all unvisited person
    do a dfs search, add unvisited person in the set
    mark visited
return the set
"""
def friendCycle3(employee_info, friend_relation):
    friend = defaultdict(set)
    for relation in friend_relation:
        """ you can do x,y = ..split()  to get the value"""
        x, y = relation.split(',')
        friend[x].add(y)
        friend[y].add(x)
    print(friend)

    def dfs(i):
        resultList.append(i)
        visited.add(i)
        for j in friend[i]:
            if j not in visited:
                dfs(j)
    #
    # visited = set()
    # resultList = []
    # for i in friend:
    #     if i not in visited:
    #         dfs(i)
    from collections import deque


    queue = deque(list(friend.keys())[0])
    resultList = []
    visited = set()
    while queue:
        person = queue.popleft()
        resultList.append(person)
        visited.add(person)
        for j in friend[person]:
            if j not in visited:
                queue.append(j)
    print(resultList)
    return len(resultList) == len(employee_info)
print(friendCycle3(s1,s2))


def countTinyPairs(a, b, k):
    if len(a) == len(b) == 0: return 0
    length = len(a)
    res = 0
    for i in range(length):
        num = str(a[i]) + str(b[length - 1 - i])
        print(num)
        # i = 0
        # while num[i] != '0':
        #     i += 1
        # print(int(num[i:]))
        if int(num[i:]) < k:
            res += 1
    return res
print(countTinyPairs([1,2], [1,2], 5))
