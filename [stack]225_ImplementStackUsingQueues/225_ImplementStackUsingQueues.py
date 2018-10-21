"""
问题：
实现栈功能

解法：
略
"""
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.insert(0,x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack.pop(0)
        return 0

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if (len(self.stack) > 0):
            return self.stack[0]
        return 0

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.stack:
            return False
        return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())     # returns 2
print(stack.pop())     # returns 2
print(stack.empty())   # returns false