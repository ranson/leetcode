"""
问题：
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
返回结果形体的总表面积。

解法：
（1）
直接求面积，从x或y方向来看，增加的面积就是相邻方块的高度差。这样不断累加即可。

（2）
要求整个图形的表面积，那么可以分解为求出每个立方体的表面积，然后减去重叠部分的面积。按照这个思路，就变得简单了。
如果某个位置的数值不是0，那么这个柱子的表面积是grid[i][j] * 4 + 2；
重叠部分的面积是两个柱子之间，高度最小的那个的高度.因为重叠使得两个柱子都变矮了，所以要把这个高度*2.
"""

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        total = 0
        preColumn = 0
        preRow = 0
        for i in range(N):
            preRow, preColumn = 0, 0
            for j in range(N):
                total += abs(grid[i][j] - preRow)
                preRow = grid[i][j]
                total += abs(grid[j][i] - preColumn)
                preColumn = grid[j][i]
                total += 2 if grid[i][j] > 0 else 0
            total += (preRow + preColumn)
        return total

solution = Solution()
grid = [[2]]
print (grid)
print (solution.surfaceArea(grid))

grid = [[1,2],[3,4]]
print (grid)
print (solution.surfaceArea(grid))

grid = [[1,0],[0,2]]
print (grid)
print (solution.surfaceArea(grid))

grid = [[1,1,1],[1,0,1],[1,1,1]]
print (grid)
print (solution.surfaceArea(grid))

grid = [[2,2,2],[2,1,2],[2,2,2]]
print (grid)
print (solution.surfaceArea(grid))