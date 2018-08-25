"""
题目大意：
给一个数组prices[]，prices[i]代表股票在第i天的售价，求出只做一次交易(一次买入和卖出)能得到的最大收益。

解法:跟53题目类同
使用动态规划，[a,b,c,d,e]为子问题，maxValue为子问题的最优解，现在添加f后为[a,b,c,d,e,f]，求的f天为卖的的最优解为f-minValue,
所以[a,b,c,d,e,f]的最优解为max(maxValue,f-minValue)
minValue只要前面计算的时候保存即可，不用再做search
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        minValue = prices[0]
        maxValue = 0
        for i in range(1,len(prices)):
            if prices[i-1]<minValue:
                minValue = prices[i-1]
            if prices[i] - minValue > maxValue:
                maxValue = prices[i] - minValue
        return maxValue

solution = Solution()
nums = [7,1,5,3,6,4]
print(solution.maxProfit(nums))
nums = [7,6,4,3,1]
print(solution.maxProfit(nums))
nums = [-2]
print(solution.maxProfit(nums))
nums = [-2,1]
print(solution.maxProfit(nums))