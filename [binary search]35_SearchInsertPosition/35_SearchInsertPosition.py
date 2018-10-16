"""
问题：
给定一个有序数组，从该数组中查找指定数字的位置，若数字不在该数组，返回应插入的位置

解法：
二分查找
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s,e = 0, len(nums)-1
        while(s <= e):
            m = (s + e)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        return s

solution = Solution()
print(solution.searchInsert([1,3,5,6], 5))
print(solution.searchInsert([1,3,5,6], 2))
print(solution.searchInsert([1,3,5,6], 7))
print(solution.searchInsert([1,3,5,6], 0))