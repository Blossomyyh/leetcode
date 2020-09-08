from collections import Counter
from collections import defaultdict

##############
# check ABC
def checkABC(a, b, c):
    if not a or not c:
        return True if not b else False
    # check b in c
    for i in b:
        if i not in c:
            return False
    # compute a and c to see longest sub is b
    dic = {}
    # ans tuple of the form (window length, left, right)
    ans = float('inf'), None, None
    # left and right pointer
    l, r = 0, 0
    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    formed = 0
    while r < len(a):
        # add one ch from right to the window
        ch = a[r]
        # if ch not in c:

        dic[ch] = dic.get(ch, 0) + 1
        #         check
        if ch in c:
            formed += 1
        while l <= r and formed == len(c):
            ch = a[l]
            if r - l + 1 < ans[0]:
                ans = r - l + 1, l, r
            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            dic[ch] -= 1
            formed -= 1
            # Move the left pointer ahead, this would help to look for a new window.
            l += 1
        r += 1
    return


# Complete the 'getSpecialSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#  3. STRING charValue


"""ord（） function"""


def normal(c, charValue):
    if charValue[ord(c) - ord('a')] == '0':
        return 1
    return 0


def getSpecialSubstring(s, k, charValue):
    left = 0
    normalCount = 0
    res = -1
    for i, c in enumerate(s):
        normalCount += normal(c, charValue)
        if normalCount > k:
            while normal(s[left], charValue) == 0:
                left += 1
            left += 1
            normalCount -= 1
        res = max(i - left + 1, res)
    return res



#####################
"""
rotate matrix

1. rotate with aligned coordinators
2. roate with rememberingg one line

"""
def rotateDiagonal(matrix, k):
    k = k % 4
    length = len(matrix)
    if k == 0:
        return matrix
    for time in range(k):
        """
        remember only need
        \\row -- length//2 + length%2
        \\col -- length//2
        """
        # only need to rotate 1/4 section
        for i in range(length//2 + length%2):
            for j in range(length//2):
                if i == j or i == length - j -1:
                    continue
                else:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[length - j - 1][i]
                    matrix[length - j - 1][i] = matrix[length - i - 1][length - j - 1]
                    matrix[length - i - 1][length - j - 1] = matrix[j][length - i - 1]
                    matrix[j][length - i - 1] = temp
    return matrix

m = [[1,   2,  3,  4,  5],  [6,   7,  8,  9, 10],  [11,12,13,14,15],  [16,17,18,19,20],  [21,22,23,24,25]]
# print(rotateDiagonal(m, 2))


###########################
"""
matrix queries

sum up the frequency of target in range(matrix[0]-[1])
"""
def matrixQueries(matrix, arrary):
    targetSet = set()
    for _, _, target in matrix:
        targetSet.add(target)
    dic = defaultdict(list)
    for target in targetSet:
        for i in range(len(arrary)):
            if arrary[i] == target:
                dic[target] = dic.get(target, [])
                dic[target].append(i)
    res  = 0
    for start, end, target in matrix:
        for index in dic[target]:
            if start <= index <= end:
                res += 1
    return res
array = [1,1,2,3,2]
matrix = [[1,2,1],[2,4,2],[0,3,1]]
# print(matrixQueries(matrix, array))


#########################
"""
 isPrefix，给两个 str array a，b，判断 b 里面的所有 str 是不是都是 a 的 str 各种组合黏在 一起而成的
Sol: 直接建立所有 a 里面 str 的 permutation 然后存入 set 里


"""


########################
"""
Max Arithmetic Length:
we can focus on interval
first find min & max interval with A
next for each possible interval try to add ele in B
    add in the front
    add at the end
    add at the middle between j-1, j


    public static int max_arithmetic_length(int[] a, int[] b) {
        HashSet<Integer> set_b = new HashSet();
        for(int n: b){
            set_b.add(n);
        }
        int min_interval = (a[0] == 0? Integer.MAX_VALUE : a[0]);
        for(int i = 1; i < a.length; i++) {
            min_interval = Math.min(min_interval, a[i] - a[i-1]);
        }
        if (min_interval == 0) {
            return -1;
        }
        // we need to make sure that the modified array has interval that less or equal to min_interval
        int i = 1;
        int result = -1;
        //System.out.println(min_interval);
        while(i <= min_interval) {
            if (min_interval % i == 0) {
                
                int tmp = try_insert(a, i, set_b);
                result = Math.max(result, tmp);     
            }
            i++;
        }
        result = (result == -1 ? -1 : result+a.length);
        return result; 
    }
    public static int try_insert(int[] a, int i, HashSet<Integer> set) {
        int result = 0;
        int front = a[0];
        int tail = a[a.length-1];

        while(true) {
            front -= i;
            if(set.contains(front)) {
                result++;
            }else {
                break;
            }
        }
        while(true) {
             tail += i;
            if(set.contains(tail)) {
                result++;
            }else {
                break;
            }
        }
        // try insert in the mid
        for(int j = 1; j < a.length; j++) {
            int low = a[j-1];
            int high = a[j];
            int tmp = 0;
            while(low + i < high) {
                if (set.contains(low+i) == false) {
                    return -1;
                }else{
                    tmp++;    
                }
                low+=i;
            }
            result+=tmp;
        }
        return result;
    }

"""
from fractions import gcd
class Solution(object):
    def bFormArithSeqLength(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        delta = [a[i] - a[i - 1] for i in xrange(1, len(a))]
        smallest = reduce(gcd, delta)
        if smallest == 1: return -1
        # in delta, determine if insertion from b make sense
        inserts = 0
        for i in xrange(len(delta)):
            if delta[i] != smallest:  # when gcd is 3, but delta is 6 or 9
                count = 1
                while (a[i] + smallest * count) in b and smallest * count < delta[i]:
                    count += 1
                if smallest * count != delta[i]:  # we failed fill in the gap between two a number
                    return -1
                else:
                    inserts += count - 1  # when gap is 9, count will be end at 3, but we only insert 2 numbers in b

        # calcu how many in b can be prepend to a
        precount = 1
        while a[0] - smallest * precount in b:
            precount += 1
        inserts += precount - 1
        # calcu how many in b can be append to a
        postcount = 1
        while a[len(a) - 1] + smallest * postcount in b:
            postcount += 1
        inserts += postcount - 1
        return inserts + len(a)

#######################
"""
subdivisor:

result should not be duplicated
"""

def divisorSubstrings(n, k):
    string = str(n)
    result = set()
    for i in range(0, len(string)-k+1):
        subNumber = int(string[i: i+k])
        print(subNumber)
        if n % subNumber == 0:
            result.add(subNumber)
    return list(result)
# print(divisorSubstrings(120, 2))
# print(divisorSubstrings(555, 1))
# print(divisorSubstrings(2345, 2))

###################
"""
 sum of string
 
 给两串字符串，每个 char 就是一个 digit，然后从后往前加起来，
 把结果放 到一个字符串输出，挺简单的。'99' + '99' = '1818'

    make two integer to string
    make 2 pointers points at the end of the string
    move ahead one by one and cal the sum of 2 digit 
    and turn it to string , append it to result
    return reverse result
"""
def sumOfString(a, b):
    i = len(a)-1
    j = len(b)-1
    result = ""
    while i>=0 and j >=0:
        sumUp = int(a[i]) + int(b[j])
        result = str(sumUp) + result
        i -= 1
        j -= 1
    if i>= 0:
        result = str(a[0:i+1]) + result
    if j>= 0:
        result = str(b[0: j+1]) + result

    return result
# print(sumOfString("99", "9999"))


####################
"""
findMinInArray

 给你一个 2d array。其中 array[i][j] = (i+1)*(j+1)。这个给定。
然后给一堆 query，有三种不同的格式： 
第一种是让你返回当前 array 中的最小值 ---amang all remaining active cells on the board
第二种是让你把某一行 disable 
第三种是把某一列 disable 当然 disable 了之后最小值就不能用了
"""
import heapq
def findMinInArray(n, m, query):
    heap = []
    for i in range(n):
        for j in range(m):
            heap.append((i+1)*(j+1))

    print(heap)
    result = []
    rowDisable, colDisable = set(), set()
    for query in queries:
        if len(query) ==1:
            heapq.heapify(heap)
            result.append(heap[0])
        elif len(query) == 2 and query[0] ==1:
#             disable row i
            row = query[1]-1
            rowDisable.add(row)
            for j in range(m):
                if j in colDisable:
                    continue
                print((j+1)*(row+1))
                heap.remove((j+1)*(row+1))
        elif len(query) == 2 and query[0] ==2:
#             disable row i
            col = query[1]-1
            colDisable.add(col)
            for i in range(n):
                if i in rowDisable:
                    continue
                print((i+1)*(col+1))
                heap.remove((i+1)*(col+1))
    print(heap)
    print(heap[-1])
    print(heapq.nlargest(2,heap))
    return result

n = 3
m =4
queries = [[0], [1,2], [0], [2,1], [0], [1,1], [0]]
# print(findMinInArray(n,m, queries))


#######################
"""
reverse digits in pairs

go a single path --- reverse each pair append to a new string and check the end
1. turn string to list
2. iterate for pairs --> odd string will have sting[i:i+2] for 'x'
3. no need to do extra modification for odd one
4. turn to string with split :)
"""
def reverseDigits(string):
    result = []
    listStr = list(string)
    for i in range(0, len(string), 2):
        pair = listStr[i: i+2]
        result += reversed(pair)
    return "".join(result)
# print(reverseDigits("72328"))


#########################
"""
diagonals sort
\
math
remember each line -- copy
sort
replace
"""
def diagonalSort(matrix):

    row  = len(matrix)
    col = len(matrix[0])
    tempDiagonal = []
    # horizontally
    for i in range(col-1, -1, -1):
        temI = i
        j = 0
        while j< row and temI < col:
            tempDiagonal.append(matrix[j][temI])
            temI += 1
            j += 1
        # tempDiagonal.sort()
        tempDiagonal.sort(reverse=True)
        j = 0
        temI = i
        while j< row and temI < col:
            matrix[j][temI] = tempDiagonal[j]
            temI += 1
            j += 1
        tempDiagonal = []

    # vertically
    for j in range(1, row):
        temJ = j
        i = 0
        while i< col and temJ < row:
            tempDiagonal.append(matrix[temJ][i])
            temJ += 1
            i += 1
        # tempDiagonal.sort()
        tempDiagonal.sort(reverse=True)

        i = 0
        temJ = j
        while i< col and temJ < row:
            matrix[temJ][i] = tempDiagonal[i]
            temJ += 1
            i += 1
        tempDiagonal = []

    return matrix
# print(diagonalSort([[8,4,1],[4,4,1], [4,8,9], [3,4,5]]))


########################
"""
longest equal subarray

0 - -1
build dictionary to record accumulated sum in array
    key - sum; value - [] store index
for each pair in value of key:
    compare j-i +1 to get maximum of result
    
    
    
        public static int longest_equal_subarray(int[] array) {
        for(int i = 0; i < array.length; i++) {
            if (array[i] == 0) {
                array[i] = -1;
            }
        }
        int n = array.length;
        int[] prefix_sums = new int[n+1];
        prefix_sums[0] = 0;
        for(int i = 1; i <= n; i++) {
            prefix_sums[i] = prefix_sums[i-1] + array[i-1];
        }
        int result = 0;
        for(int i = 0; i <= n; i++) {
            for(int j = i+1; j<= n; j++) {
                if (prefix_sums[j] == prefix_sums[i]) {
                    result = Math.max(result, j-i);
                }
            }
        }
        return result;
    }
    
"""
def longEqualSubarray(array):
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = -1
    sumUp= 0

    dictionary = defaultdict(list)
    dictionary[0].append(-1)
    for i in range(len(array)):
        sumUp += array[i]
        dictionary[sumUp] = dictionary.get(sumUp, [])
        dictionary[sumUp].append(i)

    result = 0
    for indices in dictionary.values():
        if len(indices) > 1:
            for i in range(len(indices)):
                for j in range(i+1, len(indices)):
                    result = max(result, indices[j]-indices[i])
    return result
# print(longEqualSubarray([0,1,0,1,0,0,0,1,1,1,0,1]))

######################
"""
window frame


"""
def windowFrame(n):
    first = "*"* n
    middle = "*" + " "*(n-2) + "*"
    for i in range(n):
        if i == 0 or i == n-1:
            print(first)
        else:
            print(middle)
    return
print(windowFrame(4))


########################
"""
 remove exact one digit char from string s or t, so that s < t;
input: String s1,s2 (lower case letters and digits) output: number of ways to remove the digit char.


"""