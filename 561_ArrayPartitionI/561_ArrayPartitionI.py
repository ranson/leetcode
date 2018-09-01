"""
问题：
给定一个长度为2n(偶数)的数组，分成n个小组，返回每组中较小值的和sum，使sum尽量大
解法：
先排序，将相邻两个数分为一组，每组较小数都在左边，求和即可
其实应该算贪心算法的一种方法，先加入的两个最大数，一定要组成一对才能使得sum尽量大
"""
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for i in range(len(nums)//2):
            sum+=nums[i*2]
        return sum

solution = Solution()
s1 = [1,4,3,2]
print("result")
print(solution.arrayPairSum(s1))
s1 = [1,4,3,2]
print("result")
print(solution.arrayPairSum(s1))