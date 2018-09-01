"""
问题：
矩阵转置，没什么好说的
"""
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        c = zip(*A)
        c = list(c)
        for i in range(len(c)):
            c[i] = list(c[i])
        return c

solution = Solution()
s1 = [[1,2,3],[4,5,6],[7,8,9]]
print("result")
print(solution.transpose(s1))
s1 = [[1,2,3],[4,5,6]]
print("result")
print(solution.transpose(s1))