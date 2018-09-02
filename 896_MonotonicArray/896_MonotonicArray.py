"""
问题：
判断是否为单调序列，包括递增和递减，没什么好讲的。。。
"""
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = 0
        p = 0
        for i in range(1,len(A)):
            if A[i] - A[i-1] > 0:
                n = 1
            elif A[i] - A[i-1] < 0:
                p = 1
            if n == 1 and p == 1:
                return False
        return True

solution = Solution()
s1 = [1,2,2,3]
print("result",s1)
print(solution.isMonotonic(s1))
s1 = [6,5,4,4]
print("result",s1)
print(solution.isMonotonic(s1))
s1 = [1,3,2]
print("result",s1)
print(solution.isMonotonic(s1))
s1 = [1,2,4,5]
print("result",s1)
print(solution.isMonotonic(s1))
s1 = [1,1,1]
print("result",s1)
print(solution.isMonotonic(s1))