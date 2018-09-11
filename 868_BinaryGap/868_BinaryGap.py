"""
问题：
给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。

如果没有两个连续的 1，返回 0

解法：
11的距离是1，101的距离是2.
二进制串肯定是1打头，所以距离一开始就是1.

然后查找后续是否出现1，出现1就计算新的距离，然后跟保持的最大距离做比较，更新最大距离的值

理解题目比写代码更费时间。。。
"""
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = str(bin(N))
        zCnt,maxCnt = 1,0
        for c in s[3:]:
            #print (c)
            if c == "0":
                zCnt += 1
            else:
                maxCnt = max(zCnt, maxCnt)
                zCnt = 1

        return maxCnt

solution = Solution()
N = 22
print (N)
print (solution.binaryGap(N))

N = 5
print (N)
print (solution.binaryGap(N))

N = 6
print (N)
print (solution.binaryGap(N))

N =  8
print (N)
print (solution.binaryGap(N))
# 13 2
N =  13
print (N)
print (solution.binaryGap(N))