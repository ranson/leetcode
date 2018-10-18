"""
问题：
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

解法：
深度优先遍历，拿到每一层的所有节点，然后判断该组节点是否对称
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkSym(l):
            for i in range(0, len(l) // 2):
                if l[i]  == None and l[-1-i] == None:
                    continue
                if not (l[i] and l[-1-i]):
                    return False
                if l[i].val == l[-1-i].val:
                    continue
                return False
            return True
        if root == None:
            return True
        v = []
        l = [root]
        ch,tmp = [],[]
        while (len(l) > 0):
            n = l.pop(0)
            if n:
                tmp.append(n.left)
                tmp.append(n.right)
            if len(l) == 0:
                l = tmp
                tmp = []
                if not checkSym(l):
                    return False
        return True

solution = Solution()
"""
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(2)
a.left.left = TreeNode(3)
a.left.right = TreeNode(4)
a.right.left = TreeNode(4)
a.right.right = TreeNode(3)
print(solution.isSymmetric(a))

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(2)
a.left.right = TreeNode(3)
a.right.right = TreeNode(3)
print(solution.isSymmetric(a))
"""
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
print(solution.isSymmetric(a))