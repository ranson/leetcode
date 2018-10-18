"""
问题:
层序遍历，从底部开始往上按层输出。 
解法:
广度优先遍历
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        l = [root]
        v,tmp = [],[]
        res = []
        while(len(l) > 0):
            n = l.pop(0)
            v.append(n.val)
            if n.left:
                tmp.append(n.left)
            if n.right:
                tmp.append(n.right)
            if (len(l) == 0):
                l = tmp
                tmp = []
                res.insert(0,v)
                v = []
        return res

solution = Solution()
a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)
print(solution.levelOrderBottom(a))
print(solution.levelOrderBottom(None))
