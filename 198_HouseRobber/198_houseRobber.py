"""
     * 题目大意：你是一名专业强盗，计划沿着一条街打家劫舍。每间房屋都储存有一定数量的金钱，唯一能阻止你
     * 打劫的约束条件就是：由于房屋之间有安全系统相连，如果同一个晚上有两间相邻的房屋被闯入，它们就会自
     * 动联络警察，因此不可以打劫相邻的房屋。
     *
     * 给定一列非负整数，代表每间房屋的金钱数，计算出在不惊动警察的前提下一晚上最多可以打劫到的金钱数。
     * 解题思路：动态规划（Dynamic Programming）
     * 状态转移方程：dp[i] = max(dp[i - 2], dp[i - 3]) + num[i]
     * 其中，dp[i]表示打劫到第i间房屋时累计取得的金钱最大值。
     * (第 i 个位置的 max 值是由 max(i-2, i-3) 加上 i 位置的值决定，以此类推)
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        robMax = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        robMax[0] = nums[0]
        if nums[0]>nums[1]:
            robMax[1] = nums[0]
        else:
            robMax[1] = nums[1]
        if len(nums) == 2:
            return robMax[1]
        for i in range(1,len(nums)):
            if robMax[i-2]+nums[i] > robMax[i-1]:
                robMax[i]=robMax[i-2]+nums[i]
            else:
                robMax[i] = robMax[i-1]
        return robMax[i]

solution = Solution()
nums = [1,2,3,1]#4
print(solution.rob(nums))
nums = [2,7,9,3,1]#12
print(solution.rob(nums))
nums = [-2]
print(solution.rob(nums))
nums = [-2,1]
print(solution.rob(nums))