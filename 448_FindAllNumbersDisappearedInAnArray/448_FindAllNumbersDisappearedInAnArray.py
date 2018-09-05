"""
问题：
长度为n的整形数组a中的所有数大于等于1，小于等于n，其中可能包含重复两次的数字。

输出[1, n]中不存在于数组a中的数字集合。

解法：
（1）第一个把list转set集合，然后[1,n+1]遍历，看那些元素不在集合里面
（2）理论上用bit map很容易解这个问题，但是题目要求不能开辟新的空间，
所以就把原数组作为bitmap，访问过的元素，对应位置的bitmap，将里面的元素赋值为负值。
最后遍历，不为负值的index，便为没访问到的元素。
"""
class Solution(object):
    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        setNums = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in setNums:
                res.append(i)
        return res
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            m = abs(nums[i]) - 1
            nums[m] = -nums[m] if nums[m] > 0 else nums[m]
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
solution = Solution()
nums = [4,3,2,7,8,2,3,1]
print(nums)
print(solution.findDisappearedNumbers(nums))