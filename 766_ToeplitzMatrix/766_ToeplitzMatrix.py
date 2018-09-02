"""
问题：
如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。

给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。
解法：
（1）自己的解法有点奇怪，取一个元素，然后比较它与对角线的其他元素是否相当
（2）一行一行比较，只要该行与上一行比较即可a[i][j] a[i+1][j+1]（没有实现）
（3）由于对角线上的i，j索引的差值是固定的，所以可以将索引差值作为key，内容存为value。遍历时，发现对于索引差值的value与当前值不一致时，返回false
"""
class Solution(object):
    def isToeplitzMatrix_2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        col = len(matrix[0])
        #print(matrix)
        for i in range(0,col - 1):
            pre = -1
            for j in range(0,min(rows, col - i)):
                #print (i,j,min(rows, col - i))
                if pre == -1:
                    pre = matrix[j][i]
                elif pre != matrix[j][i+j]:
                    #print(pre,matrix[j][i+j],j,i+j)
                    return False
        #print("next",i, j, min(col, rows - i))
        for i in range(0,rows - 1):
            pre = -1
            for j in range(0,min(col, rows - i)):
                #print (i,j,min(col, rows - i))
                if pre == -1:
                    pre = matrix[i][j]
                elif pre != matrix[i+j][j]:
                    return False
        return True
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
solution = Solution()
s1 = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print("result")
print(solution.isToeplitzMatrix(s1))
s1 = [
  [1,2],
  [2,2]
]
print("result")
print(solution.isToeplitzMatrix(s1))
s1 = [
  [1,2,3,4],
  [5,1,2,3]
]
print("result")
print(solution.isToeplitzMatrix(s1))
s1 = [
  [1,2],
  [5,2],
  [9,5]
]
print("result")
print(solution.isToeplitzMatrix(s1))
s1 = [[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
print("result")
print(solution.isToeplitzMatrix(s1))