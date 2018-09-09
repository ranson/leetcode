"""
问题：
将二叉树序列化为字符串，形式为"root(left)(right)"，空节点表示为"()"。所有不产生歧义的空括号可以省去。

解法：
使用递归。。。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def subStr(t):
            if t == None or t.val == None:
                return ""
            left = ""
            if t.left != None:
                left = subStr(t.left)
                left = "(" + left + ")"
            right = ""
            if t.right != None:
                right = "(" + subStr(t.right) + ")"
            if len(right) > 0 and len(left) == 0:
                left = "()"
            return str(t.val) + left + right
        return subStr(t)

solution = Solution()
#[1,2,3,4]
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)

t2.left = t4
t1.left = t2
t1.right = t3
print(solution.tree2str(t1))

#[1,2,3,None,4]
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(None)
t5 = TreeNode(4)

t2.left = t4
t2.right = t5
t1.left = t2
t1.right = t3
print(solution.tree2str(t1))