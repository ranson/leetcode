"""
问题：
实现队列

解法：
略
"""
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if (len(self.stack) > 0):
            return self.stack.pop(0)
        return 0

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if (len(self.stack) > 0):
            return self.stack[0]
        return 0

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(4)
print(obj.pop())
print(obj.peek())
print(obj.empty())