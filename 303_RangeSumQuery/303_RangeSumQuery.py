"""
问题：
给定一个数组，求指定区域的和

解法：
给定数组[a,b,c,d,e],[c,d,e]的和为[a,b,c,d,e]的和减去[a,b]的和
"""
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) <= 0:
            return
        self.sumArray = [0]*len(nums)
        self.sumArray[0] = nums[0]
        for i in range(1,len(nums)):
            self.sumArray[i]=self.sumArray[i-1]+nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i>len(self.sumArray) or j>len(self.sumArray):
            return 0
        if i == 0:
            return self.sumArray[j]
        return self.sumArray[j] - self.sumArray[i-1]

nums=[-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)
i=0
j=2
print(obj.sumRange(i,j))
i=2
j=5
print(obj.sumRange(i,j))
i=0
j=5
print(obj.sumRange(i,j))
NumArray([[[]]])
