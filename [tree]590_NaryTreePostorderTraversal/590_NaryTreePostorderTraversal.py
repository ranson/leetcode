"""
问题：
树的后续遍历

使用递归，非递归比较麻烦。。。
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def post(root):
            res = []
            if root == None:
                return []
            if len(root.children) == 0:
                return [root.val]
            for i in root.children:
                res += post(i)
            res.append(root.val)
            return res
        return post(root)

t1 = Node(3, [Node(5,[]),Node(6,[])])
t = Node(1,[t1,Node(2,[]),Node(4,[])])

solution = Solution()
res = solution.postorder(t)
print (res)