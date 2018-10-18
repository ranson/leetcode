"""
问题:
给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。
你可以返回满足此条件的任何数组作为答案。

解法:
"""

class Solution(object):
    def sortArrayByParity(self, A):
        #:type A: List[int]
        #:rtype: List[int]
        evenCnt = 0
        idx = 0
        ret = [i for i in A]
        for i in A:
            if i % 2 == 0:
                evenCnt += 1
        evenIdx = evenCnt -1
        for n in A:
            if n % 2 == 0:
                ret[evenIdx] = n
                evenIdx-=1
            else:
                #print (n,evenCnt+idx)
                ret[evenCnt+idx] = n
                idx += 1
        return ret

solution = Solution()
A = [3,1,2,4]
print (A)
print (solution.sortArrayByParity(A))
