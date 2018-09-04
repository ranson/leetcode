"""
典型的动态规划问题，给了一个数组，其中记录了每一天的股票值，可以买也可以卖，要先买才能卖，在卖的时候有交易费，返回最大获利的值。
对于每一天的，只有两个选择，买和卖。如果买的话，因为是先买才能卖，所以用前一天卖获利的最大值减去当日股票价格，与前一天买的获利值作比较，取最大。
如果卖的话，同样是先买了才能卖，所以用前一天买的最大利润减去今日价格再减去交易费用，与前一天卖的获利值比较，取最大值。
只需要遍历一遍就可以，所以时间复杂度是O(n)。
"""
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            #can switch the two lines
            hold = max(hold, cash - prices[i])
            cash = max(cash, hold + prices[i] - fee)
        return cash

solution = Solution()

prices = [1,3,7,5,10,3]
fee = 3
print (prices)
print(solution.maxProfit(prices,fee))

prices = [1, 3, 2, 8, 4, 9]
fee = 2
print (prices)
print(solution.maxProfit(prices,fee))
prices = [1, 3, 2, 8, 4, 9, 100, 101]
fee = 2
print (prices)
print(solution.maxProfit(prices,fee))

