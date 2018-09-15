"""
问题：
合并两棵二叉树。
解法：
递归遍历合并就可以
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def mergeTree(t1,t2):
            if t1 == None and t2 == None:
                return None
            if t1 == None:
                return t2
            if t2 == None:
                return t1

            val = 0
            if t1.val is not None:
                val += t1.val
            if t2.val is not None:
                val += t2.val
            print("val", t1.val, t2.val,val)
            t = TreeNode(val)
            t.left = mergeTree(t1.left,t2.left)
            t.right = mergeTree(t1.right,t2.right)
            return t
        return mergeTree(t1,t2)

solution = Solution()
"""
#
#   Tree 1                     Tree 2
#          1                         2
#         / \                       / \
#        3   2                     1   3
#       /                           \   \
#      5                             4   7
"""
#[1,2,3,4]
t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(2)
t1.left = t2
t1.right = t3

t4 = TreeNode(5)
t1.left.left = t4


#[1,2,3,None,4]
at1 = TreeNode(2)
at2 = TreeNode(1)
at3 = TreeNode(3)
at1.left = at2
at1.right = at3

at4 = TreeNode(None)
at5 = TreeNode(4)
at1.left.left = at4
at1.left.right = at5

at6 = TreeNode(7)
at1.right.right = at6

t = solution.mergeTrees(t1,at1)

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
print ("******")
showTree(t1)
print ("******")
showTree(at1)
print ("******")
showTree(t)
print("")