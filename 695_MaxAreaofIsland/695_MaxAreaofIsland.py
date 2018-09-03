"""
题目大意为：给定一个二维数组，它的全部元素为0和1，其中1代表陆地，0代表水域，并且假设数组的边缘是被水域包围的（意思是数组的边界之外的地方全是0）。
陆地的面积是相连的1的个数，只有四面有相连的1的区域才能算是一整块陆地。要求你找到这个数组中最大的陆地面积。
解法：
本解法使用深度优先遍历，访问一个元素时，递归访问其周围的元素，对于已经访问过的元素放到集合（set）里面，这样查询是否已经访问非常便利。
使用集合来记录访问记录，应该是比较常用的手法。
另外用python来实现真的是相当简洁
"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = set()

        def findArea(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in area and grid[r][c]):
                return 0
            area.add((r, c))
            tmp = (1 + findArea(r + 1,c) + findArea(r - 1,c)
                    + findArea(r ,c - 1) + findArea(r, c + 1))
            return tmp

        maxArea = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                maxArea = max(findArea(i,j), maxArea)
        return maxArea


solution = Solution()
num = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(solution.maxAreaOfIsland(num))
num = [[0,0,0,0,0,0,0,0]]
print(solution.maxAreaOfIsland(num))