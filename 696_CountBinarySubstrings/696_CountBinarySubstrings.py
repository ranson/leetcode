"""
问题：
给定01串，求0和1元素个数相等的子串个数，并且满足0和1分别分组存在。
解法：
（1）计算相邻的一组，连续0的个数a和连续1的个数b，取min(a,b)的值就是该组串的子串个数
（2）计算出所有连续0或1的值为group数组，取数组min(group[i],group[i+1])之和即为所求子串个数

"""
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre = 0
        cur = 0
        label = s[0]
        total = 0
        for c in s:
            if c == label:
                cur += 1
            else:
                total += min(cur,pre)
                pre = cur
                cur = 1
                label = c
        total += min(cur, pre)
        return total

    def countBinarySubstrings_2(self, s):
        groups = [1]
        for i in xrange(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in xrange(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans

solution = Solution()
s = "00110011"
print (s)
print(solution.countBinarySubstrings(s))

s = "10101"
print (s)
print(solution.countBinarySubstrings(s))

s = "1"
print (s)
print(solution.countBinarySubstrings(s))