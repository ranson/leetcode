"""
问题：
实现洪水填充算法
从(sr,sc)位置开始，与该位置相邻的四个位置，如果颜色与(sr,sc)的颜色相同，替换成newColor

解法：
深度遍历即可
"""
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row = len(image)
        col = len(image[0])
        key = image[sr][sc]
        if key == newColor: return image
        def flood(r,c):
            #print("ret2:", r, row, c, col)
            if not (0 <= r < row and 0 <= c < col):
                #print ("ret:",r,row,c,col)
                return
            if image[r][c] == key and (r,c):
                image[r][c] = newColor
                flood(r+1,c)
                flood(r-1,c)
                flood(r,c+1)
                flood(r,c-1)
            return
        flood(sr,sc)
        return image

solution = Solution()
input = [[1,1,1],[1,1,0],[1,0,1]]
print(solution.floodFill(input,1,1,2))
input = [[0,0,0],[0,1,1]]
print(solution.floodFill(input,1,1,1))