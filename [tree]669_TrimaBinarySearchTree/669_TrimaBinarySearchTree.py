"""
问题：
找出二叉搜索树里面再[L,R]范围内的节点，并组成新的二叉搜索树

解法：
递归节点，在范围内就增加为节点
When node.val > R, we know that the trimmed binary tree must occur to the left of the node.
Similarly, when node.val < L, the trimmed binary tree occurs to the right of the node. Otherwise, we will trim both sides of the tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def addNode(node):
            if node == None:
                return None
            #print (L, node.val, R)
            if L <= node.val <= R:
                #print (node.val)
                res = TreeNode(node.val)
                res.left = addNode(node.left)
                res.right = addNode(node.right)
                return res
            elif L > node.val:
                return addNode(node.right)
            elif R < node.val:
                return addNode(node.left)
        return addNode(root)
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
#res = solution.trimBST(t1,2,20)
#print (res)
res = solution.trimBST(t1,15,20)
print (res)