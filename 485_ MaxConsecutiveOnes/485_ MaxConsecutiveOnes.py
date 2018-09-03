"""
问题：
计算连续1的最大个数，没啥好说的
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        max1 = 0
        for i in nums:
            if i == 1:
                cur+=1
            else:
                cur = 0
            if cur > max1:
                max1 = cur
        return max1

solution = Solution()
nums = [1,1,0,1,1,1]
print(solution.findMaxConsecutiveOnes(nums))
nums = []
print(solution.findMaxConsecutiveOnes(nums))
nums = [1,1,1,1,0,1,1,1,0,1,1,1,1,1,1]
print(solution.findMaxConsecutiveOnes(nums))