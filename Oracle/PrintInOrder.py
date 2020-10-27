"""
1114. Print in Order

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously.
The input [1,2,3] means thread A calls first(),
 thread B calls second(), and thread C calls third().
  "firstsecondthird" is the correct output.

  concurrency problem
"""
'''
\\ Pair Synchronization
The dependency between pairs of jobs construct a partial order on the execution sequence

\\ locks as a synchronization tool. 
A lock has \\ two states:
    locked
    unlocked
A lock can be locked using the \\ acquire()\\ method.
released using the \\ release()\\ method.

\\ threading.Thread(target = add_profit, args = ())
'''
from threading import Lock


class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        # Wait for the first job to be done
        with self.firstJobDone:
            printSecond()
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondJobDone:
            printThird()
