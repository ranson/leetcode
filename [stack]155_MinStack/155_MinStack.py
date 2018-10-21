"""
问题：
设计一个栈，支持在常数时间内push，pop，top，和取最小值。

push(x) -- 元素x压入栈
pop() -- 弹出栈顶元素
top() -- 获取栈顶元素
getMin() -- 获取栈中的最小值

解法：
“双栈法”，栈stack存储当前的所有元素，minStack存储栈中的最小元素。
在操作元素栈stack的同时，维护最小值栈minStack。

class MinStack:
  # @param x, an integer
  # @return an integer
  def __init__(self):
    self.stack = []
    self.minStack = [] #最小值栈

  def push(self, x):
    self.stack.append(x)
    #如果 最小值栈为空，或者新增值 <= 最小值栈顶的值
    if len(self.minStack) == 0 or x <= self.minStack[-1]:
      #x入最小值栈
      self.minStack.append(x)

  def pop(self):
    #如果 栈顶值 == 最小值栈顶值
    if self.top() == self.getMin():
        #最小值栈顶元素弹出
        self.minStack.pop()
    return self.stack.pop()

  def top(self):
    return self.stack[-1]

  def getMin(self):
    return self.minStack[-1]
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]

    def getMin(self):
        """
        :rtype: int
        """
        minVal = self.stack[0]
        for c in self.stack:
            if c < minVal:
                minVal = c
        return minVal

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  #Returns -3.
print(minStack.pop())
print(minStack.top())     #Returns 0.
print(minStack.getMin())  #Returns -2.