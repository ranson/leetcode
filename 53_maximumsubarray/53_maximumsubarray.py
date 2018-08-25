"""
题目大意：
求数组的最大子数组的和

使用动态规划方法：
1. 原问题可分解为Max为[a,b,c,d,e]的最优解，cur为包含e的最优解，则[a,b,c,d,e,f]的最优解为max(max(cur+f,f),Max)
2. 然后由子问题重新构建到原问题
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax = nums[0]
        max = nums[0]
        for i in nums[1:]:
            if curMax + i < i:
                curMax = i
            else:
                curMax+=i

            if curMax > max:
                max = curMax
        return max


solution = Solution()
nums = [0]
print(solution.maxSubArray(nums))
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.maxSubArray(nums))
nums = [-2]
print(solution.maxSubArray(nums))
nums = [-2,1]
print(solution.maxSubArray(nums))