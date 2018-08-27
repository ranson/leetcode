"""
题目：
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false
解法：
Approach 1: Just return true
Alex is first to pick pile.
piles.length is even, and this lead to an interesting fact:
Alex can always pick odd piles or always pick even piles!

For example,
If Alex wants to pick even indexed piles piles[0], piles[2], ....., piles[n-2],
he picks first piles[0], then Lee can pick either piles[1] or piles[n - 1].
Every turn, Alex can always pick even indexed piles and Lee can only pick odd indexed piles.

In the description, we know that sum(piles) is odd.
If sum(piles[even]) > sum(piles[odd]), Alex just picks all evens and wins.
If sum(piles[even]) < sum(piles[odd]), Alex just picks all odds and wins.

So, Alex always defeats Lee in this game.

Approach 2: 2D DP
It's tricky when we have even number of piles of stones. You may not have this condition in an interview.

Follow-up:

What if piles.length can be odd?
What if we want to know exactly the diffenerce of score?
Then we need to solve it with DP.

dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j].
You can first pick piles[i] or piles[j].

If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
If you pick piles[j], your result will be piles[j] - dp[i][j - 1]
So we get:
dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
We start from smaller subarray and then we use that to calculate bigger subarray.
"""


class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n-1] > 0

solution = Solution()
piles = [5,3,4,5]
print(solution.stoneGame(piles))