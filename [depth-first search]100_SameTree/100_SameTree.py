"""
问题：
给定两棵二叉树，编写函数检查它们是否相等。
当且仅当两棵二叉树的结构相同并且节点值也相同时，判定为相等。

解法：
递归
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def checkTree(a,b):
            if a == None and b == None:
                return True
            elif not (a and b):
                return False
            if a.val == b.val:
                return checkTree(a.left,b.left) and checkTree(a.right,b.right)
            else:
                return False
        return checkTree(p,q)

solution = Solution()
a = TreeNode(5)
b = TreeNode(6)
c = TreeNode(7)
a.left = b
a.right = c

a1 = TreeNode(5)
b1 = TreeNode(6)
c1 = TreeNode(7)
d1 = TreeNode(8)
a1.left = b1
a1.right = c1
b1.left = d1
print(solution.isSameTree(a,a1))