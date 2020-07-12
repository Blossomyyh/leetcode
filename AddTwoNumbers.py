# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # digits-by-digits sum starting from the head of list, which contains the least-significant digit.
        #         Update carry = sum / 10carry=sum/10.
        dummy = ListNode(0)
        prev = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value // 10
            # carry, value = divmod(val1+ val2 +carry, 10)
            prev.next = ListNode(value % 10)
            prev = prev.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next



# The pseudocode is as following:
#
# Initialize current node to dummy head of the returning list.

# Initialize carry to 00.

# Initialize pp and qq to head of l1l1 and l2l2 respectively.

# Loop through lists l1l1 and l2l2 until you reach both ends.

# Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.

# Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.

# Set sum = x + y + carrysum=x+y+carry.

# Update carry = sum / 10carry=sum/10.

# Create a new node with the digit value of (sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.

# Advance both pp and qq.

# Check if carry = 1carry=1, if so append a new node with digit 11 to the returning list.

# Return dummy head's next node.