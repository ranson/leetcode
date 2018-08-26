"""
问题：
爬楼梯，每一阶楼梯都有不同的代价，找出上楼梯代价最小的走法，可以从第一阶或第二阶开始，每次可以走一阶或两阶

解法：
如果我们用一个数组dp[]来存放到达每一层所需要的花费值。则则最终结果是求dp[cost.length]的值。
因为每次可以走1层或者2层，并且可以从0或者从1开始，所以可以得到dp[0]为0，dp[1]为0。
从2开始，dp[i]可以由通过dp[i-2]走2层或者通过dp[i-1]走一层到达，
而这i-2和i-1层所要花费的值分别为cost[i-2]和cost[i-1]，
所以，dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])。
该算法的空间复杂度为O(n)，时间复杂度为O(n)。
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        result = [0] * len(cost)
        result[0] = cost[0]
        result[1] = cost[1]
        for i in range(2,len(cost)):
            if result[i-2]< result[i-1]:
                result[i] = result[i-2]+cost[i]
            else:
                result[i] = result[i-1]+cost[i]
        if result[len(cost) - 1] < result[len(cost) - 2]:
            return result[len(cost) - 1]
        else:
            return result[len(cost) - 2]


solution = Solution()
cost = [10, 15, 20]
print(solution.minCostClimbingStairs(cost))
cost = [10, 15]
print(solution.minCostClimbingStairs(cost))
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(solution.minCostClimbingStairs(cost))
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100]
print(solution.minCostClimbingStairs(cost))