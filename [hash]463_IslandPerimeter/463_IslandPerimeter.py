"""
问题：
给定一个二维地图，1表示陆地，0表示水域。单元格水平或者竖直相连（不含对角线）。地图完全被水域环绕，只包含一个岛屿（也就是说，一个或者多个相连的陆地单元格）。岛屿没有湖泊（岛屿内部环绕的水域）。单元格是边长为1的正方形。地图是矩形，长宽不超过100。计算岛屿的周长。

解法：
（1）存在边表示为相邻块的和为1，记录所有相邻块和为1的组合
（2）每一个陆地单元格的周长为4，当两单元格上下或者左右相邻时，令周长减2。
class Solution(object):
    def islandPerimeter(self, grid):
        h = len(grid)
        w = len(grid[0]) if h else 0
        ans = 0
        for x in range(h):
            for y in range(w):
                if grid[x][y] == 1:
                    ans += 4
                    if x > 0 and grid[x - 1][y]:
                        ans -= 2
                    if y > 0 and grid[x][y - 1]:
                        ans -= 2
        return ans
"""
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s = set()
        sum = 0
        length = len(grid[0])
        grid.insert(0,[0] * (length + 2))
        for line in grid[1:]:
            line.insert(0,0)
            line.append(0)
        grid.append([0] * (len(grid[0])))
        #print (grid)
        for i in range(1,len(grid) - 1):
            #print (i)
            for j in range(1,len(grid[0]) - 1):
                #print(i,j)
                if grid[i][j] + grid[i][j+1] == 1:
                    s.add(((i,j),(i,j+1)))
                if grid[i][j] + grid[i + 1][j] == 1:
                    s.add(((i,j),(i+1,j)))
                if grid[i][j] + grid[i][j-1] == 1:
                    s.add(((i, j-1),(i, j)))
                if grid[i][j] + grid[i -1][j] == 1:
                    s.add(((i-1, j),(i, j)))
                #print (s)
        #print (s)
        return len(s)

solution = Solution()
input = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print (solution.islandPerimeter(input))
input = [[1]]
print (solution.islandPerimeter(input))
input = [[1,0]]
print (solution.islandPerimeter(input))