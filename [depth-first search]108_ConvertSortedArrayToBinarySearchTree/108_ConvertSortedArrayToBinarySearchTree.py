"""
问题：
给你一个升序的序列，根据这个序列来构造一个平衡二叉树。

解法：
解题思路就是先找到根节点，然后递归找到左右子节点。 
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def buildNode(n):
            if n:
                pos = len(n)//2
                t = TreeNode(n[pos])
                t.left = buildNode(n[0:pos])
                if pos + 1 < len(n):
                    t.right = buildNode(n[pos+1:len(n)])
                return t
            else:
                return None
        return buildNode(nums)

solution = Solution()
k = solution.sortedArrayToBST([-10,-3,0,5,9])
print( "hihihi" )
