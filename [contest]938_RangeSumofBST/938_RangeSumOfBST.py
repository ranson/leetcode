"""
问题：
返回树中rang再[L,R]的元素之和

解法：

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root == None:
            return 0
        v = 0
        v += self.rangeSumBST(root.left, L, R)
        v += self.rangeSumBST(root.right, L, R)
        if root.val <= R and root.val >= L:
            v += root.val
        return v

t = TreeNode(10)
t.left = TreeNode(5)
t.right = TreeNode(15)
t.left.left = TreeNode(3)
t.left.right = TreeNode(7)
t.right.left = None
t.right.right = TreeNode(18)
solution = Solution()
print (solution.rangeSumBST(t,7,15))