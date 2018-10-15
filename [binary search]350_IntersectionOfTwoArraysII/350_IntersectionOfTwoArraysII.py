"""
问题：
给定两个数组，编写函数计算它们的交集。

解法：
使用collections后，使用&求交集即可
"""
import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        cnt1 = collections.Counter(nums1)
        cnt2 = collections.Counter(nums2)
        return [x for x in (cnt1 & cnt2).elements()]

solution = Solution()
print(solution.intersect([1,2,2,1], [2,2]))
print(solution.intersect([4,9,5], [9,4,9,8,4]))