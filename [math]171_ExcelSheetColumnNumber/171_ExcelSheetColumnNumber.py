"""
问题：
给定一个出现在Excel表格中的列标题，返回其对应的列号。
解法：
水题，26进制转化为10进制
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        multiples = 1
        for i in s[::-1]:
            total += (ord(i) - ord("A") + 1) * multiples
            multiples = multiples * 26
        return total

solution = Solution()
s = "A"
print (s)
print(solution.titleToNumber(s))
s = "AB"
print (s)
print(solution.titleToNumber(s))
s = "ZY"
print (s)
print(solution.titleToNumber(s))
