"""
问题：
跟559类似，求树的深度。。。
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getTreeDepth(node):
            if node == None:
                return 0
            if node.left == None and node.right == None:
                return 1
            depth = 0
            depth = max(depth, getTreeDepth(node.left), getTreeDepth(node.right))
            return depth + 1
        return getTreeDepth(root)

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
print (solution.maxDepth(t1))