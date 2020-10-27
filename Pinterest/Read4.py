"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

'''
\\ make use of space
    use queue to store all character
    while count<n:
        check queue
        if not empty:
            get one cha from pop queue
        else
            read4 and append cha to queue
            if ==0
                break

'''
class Solution(object):
    def __init__(self):
        self.left = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        count = 0

        while count<n:
            if self.left:
                count += 1
                buf[count] = self.left.pop(0)
            else:
                buf4 = ['']*4
                readint = read4(buf4)
                if readint ==0:
                    # end of the file
                    break
                else:
                    self.left += buf4[:readint]

        return count


index = 0
string = 'abcdefg'
# def read4(buf):
#     global index
#     i = 0
#     while i<4 and index<len(string):
#         buf[i] = string[index]
#         index += 1
#         i+=1
#     return i

def read4(reads):
    global index

    count = 0
    while count < 4 and index < len(string):
        reads[count] = string[index]
        count += 1
        index += 1
    return count


a = Solution()
buf = [0] * 100
print(a.read(buf, 3))
print(a.read(buf, 4))
print(a.read(buf, 3))
# 3 4 0