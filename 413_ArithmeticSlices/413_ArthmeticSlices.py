"""
题目：
给你一串数字，返回这串数字中能够构成等差数列的子串的数目。
解法：
动态规划的思想,[a,b,c,d,e]中子串个数为n,[a,b,c,d,e,f]的子串个数为n+(包含e元素的最长等差子串长度-2)
"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n <= 2:
            return 0
        diff = A[1] - A[0]
        arrCnt = 1
        sum = 0

        for i in range(2,n):
            if A[i] - A[i-1] == diff:
                arrCnt+=1
            else:
                diff = A[i] - A[i-1]
                arrCnt = 1
            if arrCnt != 1:
                sum += (arrCnt - 1)
        return sum

solution = Solution()
piles = [1, 2, 3, 4]
print(solution.numberOfArithmeticSlices(piles))
piles = [1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2]
print(solution.numberOfArithmeticSlices(piles))
piles = [1, 1, 2, 5, 7]
print(solution.numberOfArithmeticSlices(piles))