# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def buildTree(root):
            if root:
                yield from buildTree(root.left)
                yield root.val
                yield from buildTree(root.right)
        ans = cur = TreeNode(None)
        for v in buildTree(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right



"""
#
#   Tree 1
#          10
#         /  \
#        5    15
#       / \  / \
#      2  8  12  20
#        / \
#       6   9
"""

t1 = TreeNode(10)
t1.left = TreeNode(5)
t1.right = TreeNode(15)

t1.left.left = TreeNode(2)
t1.left.right = TreeNode(8)
t1.left.right.left = TreeNode(6)
t1.left.right.right = TreeNode(9)

t1.right.left = TreeNode(12)
t1.right.right = TreeNode(20)

solution = Solution()
res = solution.increasingBST(t1)
print (res)