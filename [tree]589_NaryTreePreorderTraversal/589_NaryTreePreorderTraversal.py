
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def showTree(root):
            if root == None:
                return []
            lNode = []
            for i in root.children:
                lNode = lNode + showTree(i)
            lNode = [root.val] + lNode
            return lNode
        return showTree(root)

"""
#
#   Tree 1                     
#             1      
#         /   |   \
#        3    2    4
#       / \  
#      5  6
"""
t1 = Node(3, [Node(5, []), Node(6, [])])
t = Node(1, [t1, Node(2, []), Node(4, [])])

solution = Solution()
res = solution.preorder(t)
print (res)