"""
问题：
求每一层节点的平均值

解法：
可以使用两个list调换使用，一个存该层的节点，一个存下一层节点，但该层节点遍历完后，用下一层节点替换后，继续遍历
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def averageOfLevels_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodeCnt = 1
        totalNode = 1
        nextNode = 0
        lNode = []
        if root:
            lNode.append(root)
        levelSum = 0
        levels = []
        while(len(lNode) > 0):
            #print (len(lNode), nextNode, totalNode, nodeCnt)
            node = lNode.pop(0)
            levelSum += node.val
            nodeCnt -= 1

            if node.left:
                nextNode += 1
                lNode.append(node.left)
            if node.right:
                nextNode += 1
                lNode.append(node.right)
            if nodeCnt == 0:
                levels.append(levelSum/totalNode)
                totalNode = nextNode
                nodeCnt = totalNode
                nextNode = 0
                levelSum = 0
        return levels

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        totalNode = 1
        lNode = []
        if root:
            lNode.append(root)
        levelSum = 0
        levels = []
        tmp = []
        while(len(lNode) > 0):
            #print (len(lNode), nextNode, totalNode, nodeCnt)
            node = lNode.pop(0)
            levelSum += node.val

            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if len(lNode) == 0:
                levels.append(levelSum*1.0/totalNode)
                totalNode = len(tmp)
                lNode = tmp
                tmp = []
                levelSum = 0
        return levels
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
print (solution.averageOfLevels(t1))