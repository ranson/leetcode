"""
问题：
计算树的深度

递归就好了。。。
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def getTreeDepth(node):
            if node == None:
                return 0
            if len(node.children) == 0:
                return 1
            depth = 0
            for i in node.children:
                depth = max(depth, getTreeDepth(i))
            return depth + 1
        return getTreeDepth(root)