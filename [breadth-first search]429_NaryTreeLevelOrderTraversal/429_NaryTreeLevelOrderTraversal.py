"""
问题：
多叉树广度遍历
解法：
理解错意思了。。。
理解为从数组重建树结构了。。。
哎。。。
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        children = [root]
        res = []
        tmp = []
        val = []
        while (len(children) > 0):
            node = children.pop(0)
            val.append(node.val)
            if node.children and len(node.children) > 0:
                tmp = tmp + node.children

            if len(children) == 0:
                children = tmp
                res.append(val)
                tmp = []
                val = []
        return res

solution = Solution()
n = solution.levelOrder(
    Node(1, [Node(10, [Node(5, None), Node(0, None)]), Node(3, [Node(6, None)])])
)
print (n)