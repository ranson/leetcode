"""
问题：
行交换，然后取反
解法：
class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in xrange((len(row) + 1) / 2):

                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.

                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
"""
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in range(len(row) // 2):
                tmp = row[i]^1
                row[i] = row[len(row) - i - 1]^1
                row[len(row) - i - 1] = tmp
            if len(row) % 2 != 0:
                row[len(row)//2] = row[len(row)//2]^1
        return A

a = 1
print (a^1)
a = 0
print (a^1)

solution = Solution()
s1 = [[1,1,0],[1,0,1],[0,0,0]]
print("result")
print(solution.flipAndInvertImage(s1))
s1 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print("result")
print(solution.flipAndInvertImage(s1))