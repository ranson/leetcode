"""
问题：
二叉搜索树，查找结点，二分查找即可。

"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        l = []
        l.append(root)
        while(len(l)>0):
            node = l.pop(0)
            if node.val == val:
                return node
            if node.right and node.val < val:
                l.insert(0, node.right)
            if node.left and node.val > val:
                l.insert(0, node.left)
        return None

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
t1.right.left = TreeNode(6)
t1.right.right = TreeNode(9)

t1.left.right.left = TreeNode(12)
t1.left.right.right = TreeNode(20)

solution = Solution()
target = solution.searchBST(t1,2)
print(target)
target = solution.searchBST(t1,12)
print(target)

def showTree(t):
    l = []
    print (t.val)
    l.append(t.left)
    l.append(t.right)
    while (len(l) > 0):
        t = l.pop(0)
        if t is not None:
            print(t.val)
            l.append(t.left)
            l.append(t.right)
        else:
            print ("null")