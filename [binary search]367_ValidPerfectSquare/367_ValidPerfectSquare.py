"""
问题：
给定一个正整数num，编写函数：如果num是完全平方数，返回True，否则返回False。
注意：不要使用任何内建函数，例如sqrt。
测试用例如题目描述。

解法：
二分查找
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        s,e = 0, num
        while (s <= e):
            m = (s + e)//2
            v = m * m
            if v == num:
                return True
            elif v > num:
                e = m - 1
            else:
                s = m + 1
        return False

solution = Solution()
print(solution.isPerfectSquare(16))
print(solution.isPerfectSquare(14))