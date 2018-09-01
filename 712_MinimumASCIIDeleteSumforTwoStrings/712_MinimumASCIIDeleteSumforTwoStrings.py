"""
问题：
给定两个字符串，删除若干个字符使得两个字符串相等，求最小删除的asic码字的和
解法：
Let dp[i][j] be the answer to the problem for the strings s1[i:], s2[j:].

When one of the input strings is empty, the answer is the ASCII-sum of the other string. We can calculate this cumulatively using code like dp[i][s2.length()] = dp[i+1][s2.length()] + s1.codePointAt(i).

When s1[i] == s2[j], we have dp[i][j] = dp[i+1][j+1] as we can ignore these two characters.

When s1[i] != s2[j], we will have to delete at least one of them. We'll have dp[i][j] as the minimum of the answers after both deletion options.

The solutions presented will use bottom-up dynamic programming.
"""

class Solution(object):
    def minimumDeleteSum_NG(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def sumasic(s1,s2):
            if s1 == s2:
                #print(s1,">>>",s2)
                return 0
            sum = 0
            if len(s1) == 1 and len(s2) == 1:
                #print(s1, ">>>", s2)
                return ord(s1[0]) + ord(s2[0])
            if len(s1) == 0:
                #print(">>>",s2)
                for i in s2:
                    sum += ord(i)
                return sum
            elif len(s2) == 0:
                #print(">>>",s1)
                for i in s1:
                    sum += ord(i)
                return sum
            if len(s1) > len(s2):
                ss1 = s1
                ss2 = s2
            else:
                ss1 = s2
                ss2 = s1
            sum = len(ss1) * 122
            #print("[in]", ss1, ss2, sum)
            for n in range(0,len(ss1)):
                #print (len(ss1),n)
                value = ord(ss1[n])
                nss1 = ss1[0:n] + ss1[n+1:len(ss1)]
                res = sumasic(nss1,ss2) + value
                if res < sum:
                    sum = res
            #print ("[out]", ss1,ss2,sum)
            return sum
        return sumasic(s1,s2)

    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0] * (len(s2) + 1) for i in range(len(s1)+1)]
        for i in range(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for i in range(len(s2) - 1, -1, -1):
            dp[len(s1)][i] = dp[len(s1)][i+1] + ord(s2[i])
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                if (s1[i] == s2[j]):
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
        return dp[0][0]
solution = Solution()
s1 = "sea"
s2 = "eat"
print("result")
print(solution.minimumDeleteSum(s1,s2))
s1 = "delete"
s2 = "leet"
print("result")
print(solution.minimumDeleteSum(s1,s2))