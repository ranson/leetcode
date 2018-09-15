"""
问题：
举个例子，给定一个如上图所示的树，其叶值序列为 (6, 7, 4, 9, 8) 。
如果两个二叉树的叶值序列相同，我们就认为它们是 叶相似的。
如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，返回 true；否则返回 false 。

解法：
深度遍历，保持叶节点即可
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def findLeaf(root):
            leafs = []
            lnode = []
            lnode.append(root)
            while (len(lnode) > 0):
                node = lnode.pop(0)
                if node.left is None and node.right is None:
                    leafs.append(node.val)
                else:
                    if node.right is not None:
                        lnode.insert(0, node.right)
                    if node.left is not None:
                        lnode.insert(0,node.left)

            #print(leafs)
            return leafs

        return True if findLeaf(root1) == findLeaf(root2) else False
    def leafSimilar_2(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dps(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dps(node.left)
                yield from dps(node.right)
        return list(dps(root1)) == list(dps(root2))

solution = Solution()
"""
#
#   Tree 1                     
#           3      
#         /  \      
#        5    1  
#       / \  / \    
#      6  2  9  8     
#        / \
#       7   4
"""

t1 = TreeNode(3)
t1.left = TreeNode(5)
t1.right = TreeNode(1)

t1.left.left = TreeNode(6)
t1.left.right = TreeNode(2)
t1.right.left = TreeNode(9)
t1.right.right = TreeNode(8)

t1.left.right.left = TreeNode(7)
t1.left.right.right = TreeNode(4)

t2 = TreeNode(3)
t2.left = TreeNode(5)
t2.right = TreeNode(1)

t2.left.left = TreeNode(6)
t2.left.right = TreeNode(2)
t2.right.left = TreeNode(9)
t2.right.right = TreeNode(8)

t2.left.right.left = TreeNode(7)
t2.left.right.right = TreeNode(4)
print (solution.leafSimilar(t1,t2))

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