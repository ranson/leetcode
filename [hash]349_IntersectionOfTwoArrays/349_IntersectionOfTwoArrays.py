"""
问题：
求交集

解法：
求交集
"""
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = set(nums1)
        n2 = set(nums2)
        return list(n1 & n2)

solution = Solution()
print(solution.intersection([1,2,2,1], [2,2]))
print(solution.intersection([4,9,5], [9,4,9,8,4]))