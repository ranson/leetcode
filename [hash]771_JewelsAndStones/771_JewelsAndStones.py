"""
问题：
给定字符串J和S，求S中在J中出现的字符总数。
解法：
暴力遍历
"""
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s = set(list(J))
        cnt = 0
        for ch in S:
            if ch in s:
                cnt += 1
        return cnt

solution = Solution()
print(solution.numJewelsInStones("aA","aAAbbbb"))
print(solution.numJewelsInStones("z", "ZZ"))