"""
问题：
给定一组点，求解用其中三个点构成的最大面积的三角形的面积

解法：
遍历所有三个点能够构成的三角形。
面积计算如下：
A = 1/2 * |x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)|
一定记得取绝对值，不然会出错
"""
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def computerArea(ps):
            if len(ps)!= 3:
                print("len error",len(ps))
                return 0
            x1 = ps[0][0]
            y1 = ps[0][1]
            x2 = ps[1][0]
            y2 = ps[1][1]
            x3 = ps[2][0]
            y3 = ps[2][1]

            #print (x3*(y1-y2))
            return abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2.0
        ps = []
        maxArea = 0
        for i in range(len(points)):
            ps.append(points[i])
            for j in range(i+1,len(points)):
                ps.append(points[j])
                for k in range(j+1,len(points)):
                    ps.append(points[k])
                    maxArea = max(computerArea(ps),maxArea)
                    #print(ps,maxArea)
                    ps.pop(2)
                ps.pop(1)
            ps.pop(0)
        return maxArea

solution = Solution()
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(points)
print(solution.largestTriangleArea(points))