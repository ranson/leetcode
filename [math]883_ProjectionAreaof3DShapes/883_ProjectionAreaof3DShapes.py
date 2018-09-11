"""
问题：
给出了一个方阵，方阵里面的数值是柱子的高度，求三视图所有的阴影部分的面积。

解法：
俯视图投影就是不为0的柱子的个数，主视图、侧视图是当前视图柱子的最高值求和
"""
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        maxArray = [0] * len(grid[0])
        for line in grid:
            for i,num in enumerate(line):
                if num > maxArray[i]:
                    maxArray[i] = num
                total += 1 if num > 0 else 0
            total += max(line)
        #print ("maxArray", maxArray)
        total += sum(maxArray)
        return total

solution = Solution()
grid = [[2]]
print (grid)
print ("Result",solution.projectionArea(grid))

grid = [[1,2],[3,4]]
print (grid)
print ("Result",solution.projectionArea(grid))

grid = [[1,0],[0,2]]
print (grid)
print ("Result",solution.projectionArea(grid))

grid = [[1,1,1],[1,0,1],[1,1,1]]
print (grid)
print ("Result",solution.projectionArea(grid))

grid = [[2,2,2],[2,1,2],[2,2,2]]
print (grid)
print ("Result",solution.projectionArea(grid))