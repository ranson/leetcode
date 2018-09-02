"""
问题：
reshape矩阵，这个没啥好说的
"""
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        res = [[0] * c for i in range(r)]
        row = len(nums)
        col = len(nums[0])
        #print ("row",row,"col",col)
        for i in range(row):
            for j in range(col):
                #print (i,j,(i*row + j)//c,(i*row + j)%c  )
                res[(i*col + j)//c][(i*col + j)%c] = nums[i][j]
        return res


solution = Solution()
nums = [[1],[2],[3],[4]]
r = 2
c = 2
print(solution.matrixReshape(nums, r, c))
nums = [[1,2],
 [3,4]]
r = 2
c = 4
print(solution.matrixReshape(nums, r, c))
