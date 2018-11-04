"""
问题：
这道跟之前那道Best Time to Buy and Sell Stock 买卖股票的最佳时间很类似，但都比较容易解答。
这道题由于可以无限次买入和卖出。

解法：
我们都知道炒股想挣钱当然是低价买入高价抛出，那么这里我们只需要从第二天开始，
如果当前价格比之前价格高，则把差值加入利润中，因为我们可以昨天买入，今日卖出，
若明日价更高的话，还可以今日买入，明日再抛出。以此类推，遍历完整个数组后即可求得最大利润。代码如下：
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit