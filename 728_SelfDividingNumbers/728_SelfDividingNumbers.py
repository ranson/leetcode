"""
问题：
“自整除数”是指可以被自己的每一位数整除的数字。
给定左右边界范围，求范围内的所有自整除数。

解法：
如字面意思，取所有整数，然后取整数的各个位循环除即可
"""
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            st = str(i)
            badd = True
            for c in st:
                if c == '0' or i % (int(c)) != 0:
                    badd = False
                    break;
            if badd:
                res.append(i)
        return res

solution = Solution()
left = 1
right = 22
print (left,right)
print (solution.selfDividingNumbers(left,right))
