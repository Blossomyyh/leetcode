#####################

# stack
#
# empty() – Returns whether the stack is empty – Time Complexity : O(1)
# size() – Returns the size of the stack – Time Complexity : O(1)
# top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
# push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
# pop() – Deletes the top most element of the stack – Time Complexity : O(1)
#
######################

"""
1. list implementation of stack
"""

stack = []


# append() function to push
stack.append(1)
stack.append(2)

# stack[-1] present top
print("Top: ", stack[-1])

print("initial: ")
print(stack)

# pop() fucntion to pop
# LIFO order
stack.pop()
print("final: ")
print(stack)


"""
2. collections.deque
"""
from collections import deque
# deque means double ended queue

stack = deque()

# append() function to push
stack.append(1)
stack.append(2)
print("initial: ")
print(stack)

# pop() fucntion to pop
# LIFO order
stack.pop()
print("final: ")
print(stack)




"""
3. queue of LifoQueue

decide the size
"""

# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking.
# qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull.


#Last in First out
from queue import LifoQueue

stack = LifoQueue(maxsize = 3)
# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

####
""" get() fucntion to pop !!!!"""
#####
# element from stack in
# LIFO order
print('\nElements poped from the stack')
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())