"""
问题：
给定一个数num，返回0 ≤ i ≤ num的所有数的二进制表示形式中包含的‘1’的个数。
解法：
动态规划的解法，i的二进制个数分解为求i/2的二进制个数+ i%2
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]*(num+1)
        result[0] = 0
        i = 1
        for i in range(1,num+1):
            result[i] = result[int(i/2)] + i%2
        return result

solution = Solution()
num = 2
print(solution.countBits(num))
num = 5
print(solution.countBits(num))
num = 10
print(solution.countBits(num))
num = 11
print(solution.countBits(num))