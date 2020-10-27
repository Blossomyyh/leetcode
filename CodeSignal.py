"""
a = [1, 3, 5, 6, 4, 2], the output should be alternatingSort(a) = true.
The new array b will look like [1, 2, 3, 4, 5, 6], which is in strictly ascending order, so the answer is true.

"""
def alternatingSort(a):
    if not a: return False
    if len(a) == 1: return True
    start, end = 0, len(a)-1
    prev = a[start]
    while start<=end:
        if start ==0:
            if a[end]>prev:
                start += 1
                end -= 1
                continue
            else:
                return False
        elif start == end:
            if a[start]>prev:
                return True
            else:
                return False
        else:
            if prev<a[start]<a[end]:
                prev = a[end]
                start += 1
                end -= 1
                continue
            else:
                return False
    return True


from collections import defaultdict


def meanGroups(a):
    dictionary = defaultdict(list)
    for i, l in enumerate(a):
        mean = sum(l) / len(l)
        dictionary[mean].append(i)
    # print(dictionary)

    result = []
    for group in dictionary.values():
        result.append(list(group))
    return result

print(meanGroups([[0,1]]))

s = "0001"
i = int(s)
print(i)


"""
For a = [10, 2], the output should be concatenationsSum(a) = 1344.

a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.
So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

For a = [8], the output should be concatenationsSum(a) = 88.

There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.

"""

def concatenationsSum(a):
    if not a: return 0
    sum = 0
    for i in range(len(a)):
        for j in range(len(a)):
            l = len(str(a[j]))
            concaten = a[i]*(10**l) + a[j]

            sum += int(concaten)
    return sum


"""
a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]

meanGroups(a) = [[0, 4],
                 [1],
                 [2, 3]]
mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
mean(a[1]) = (4 + 4) / 2 = 4;
mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
mean(a[3]) = (2 + 3) / 2 = 2.5;
mean(a[4]) = (3 + 3 + 3) / 3 = 3
"""
from collections import defaultdict
# mean groups
def meanGroups(a):
    dictionary = defaultdict(list)
    for i, l in enumerate(a):
        mean = sum(l) / len(l)
        dictionary[mean].append(i)
    # print(dictionary)

    result = []
    for group in dictionary.values():
        result.append(list(group))
    return result

"""
For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the resulting array after the mutation will be [4, 5, -1, 2, 1].



"""
def mutateTheArray(n, a):
    if not a: return 0
    if len(a) == 1: return a
    if len(a) == 2: return [a[0]+a[1],a[0]+a[1]]
    b = []
    for i in range(len(a)):
        if i == 0:
            b.append(a[0]+a[1])
        elif i == len(a)-1:
            b.append(a[len(a)-1] + a[len(a)-2])
        else:
            b.append(a[i-1]+a[i]+a[i+1])
    return b

print(int("011"))
#11
def countTinyPairs(a, b, k):
    if len(a)==0: return 0
    if k<0: return 0
    res = 0
    n = len(a)
    for i in range(n):
        num = str(a[i])+str(b[n-i-1])

        if k > int(num):
            res +=1
    return res


from collections import Counter

########
"""
1. count
2. count-- after append
3. count== ord== then first string first
"""
def mergeStrings(s1, s2):
    i, j = 0, 0
    count1 = Counter(s1)
    count2 = Counter(s2)
    result = ""

    def compare(c1, c2):
        if count1[c1] < count2[c2]:
            return 1
        elif count1[c1] > count2[c2]:
            return -1
        elif count1[c1] == count2[c2]:
            if ord(c1) < ord(c2):
                return 1
            elif ord(c1) == ord(c2):
                return 1
            elif ord(c1) > ord(c2):
                return -1

    while i < len(s1) and j < len(s2):
        res = compare(s1[i], s2[j])
        if res == 1:
            result += s1[i]
            count1[s1[i]] -= 1
            i += 1

        else:
            result += s2[j]
            count2[s2[j]] -= 1
            j += 1

    if i < len(s1):
        result += s1[i:]
    if j < len(s2):
        result += s2[j:]

    return result



def concatenationsSum(a):
    if not a: return 0
    sum = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            num1 = a[i]
            num2 = a[j]
            len1, len2 = 0, 0
            while num1:
                len1 += 1
                num1 = num1//10
            concaten = a[j]*(10**len1) + a[i]
            sum += concaten
            # print(concaten)
            if i !=j:
                while num2:
                    len2 += 1
                    num2 = num2//10
                concaten = a[i]*(10**len2) + a[j]
                sum += concaten
                # print(concaten)
    return sum



def concatenationsSum(a):
    if not a: return 0
    sum = 0
    newlist = [ str(i) for i in a]
    for i in range(len(a)):
        for j in range(i, len(a)):
            concaten = newlist[j] + newlist[i]
            sum += int(concaten)
            # print(concaten)
            if i !=j:
                concaten = newlist[i] + newlist[j]
                sum += int(concaten)
                # print(concaten)
    return sum




#################
import collections


def concatenationsSum(a):
    sum = 0
    sumall = 0
    dic = collections.defaultdict(int)
    for i in range(len(a)):
        string = str(a[i])
        n = len(string)
        dic[n] += 1
        sumall += a[i]

    for i in range(len(a)):
        for k, v in dic.items():
            sum += a[i] * (10 ** k) * v
        sum += sumall
    return sum


from collections import defaultdict

def duplicationsOnSegment(A):
    result = 0
    for i in range(0,len(A)):
        counter = 0
        hash = defaultdict (int)
        for j in range (i, len(A)):
            hash[A[j]] += 1
            if hash[A[j]] == 2:
                counter += 1
            if counter != 0 and counter == len(hash):
                result += 1
    return result


################
# Minesweeper

# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
#
#
# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]

def minesweeper(matrix):
    ret = []
    w = len(matrix[0])
    dic = {True:1, False:0}
    newMatrix = []
    newMatrix.append([])
    newMatrix.append([])
    for x in range(len(matrix[0])+2):
        newMatrix[0].insert(0,False)
        newMatrix[1].append(False)
    for y in matrix:
        y.append(False)
        y.insert(0,False)
        newMatrix.insert(-1,y)

    for i in range(len(matrix)):
        ret.append([])
        for j in range(w):
            print(newMatrix[i+2][j+2])
            k = int(dic[newMatrix[i][j]]) + int(dic[newMatrix[i][j+1]]) + int(dic[newMatrix[i][j+2]]) + int(dic[newMatrix[i+1][j]]) + int(dic[newMatrix[i+1][j+2]]) + int(dic[newMatrix[i+2][j]]) + int(dic[newMatrix[i+2][j+1]]) + int(dic[newMatrix[i+2][j+2]])
            ret[i].append(k)
    return ret
def minesweeper(matrix):
    r = []

    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[0]):
                        l += matrix[i + x][j + y]

            r[i].append(l)
    return r