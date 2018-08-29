"""
问题：
给定一个字符串，你的任务是计算在该字符串中有多少个回文子串。
解法：
1， two pointers，以每个character为中心或者以两个character之间的位置为中心向左右两边扩散， 找回文。
2， 用dp，套路理解完之后就是怎么套入不同的问题，比如这个，不让你找最长回文子串，而是找不同回文的个数，
那么dp解法中只要当dp[i][j] == true 时， count++即可，two pointers做法就有点变化了。
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        subStrings = [[0] * n for i in range(n)]
        res = 0
        for i in range(n):
            subStrings[i][i] = 1
        for i in range(0, n):
            for j in range(i,-1,-1):
                if s[i] == s[j]:
                    if i-j <3 or subStrings[j+1][i-1]>0:
                        #print (i,j)
                        subStrings[j][i]  = 1
                        res+=1
        return res

solution = Solution()
piles = "abc"
print(solution.countSubstrings(piles))
piles = "aaa"
print(solution.countSubstrings(piles))
piles = "noon"
print(solution.countSubstrings(piles))
piles = "gbcdeg"
print(solution.countSubstrings(piles))