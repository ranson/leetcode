"""
问题：
将0元素放到数组最末尾，并且不改变非0元素的顺序

解法：
(1)先找到0元素的位置，在0元素位置的后面找到非0元素的位置，做交换。然后从0元素位置+1继续寻找0元素。比较直观，却不适合写代码
(2)用lastNoneZeros记录已经遍历非0元素的个数，找到非0元素后直接覆盖到lastNoneZeros的位置即可。思路清晰，易于实现。
"""
class Solution(object):
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        s0 = 0
        sn = 1
        while s0 < len(nums) and sn < len(nums):
            if nums[s0] != 0:
                s0+=1
                continue
            else:
                if sn <= s0:
                    sn = s0 + 1
                    continue
            if nums[sn] == 0:
                sn+=1
                continue
            if nums[s0] == 0 and nums[sn] != 0:
                tmp = nums[s0]
                nums[s0] = nums[sn]
                nums[sn] = tmp
                s0+=1
                sn = s0

        return nums
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastNoneZeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNoneZeros] = nums[i]
                lastNoneZeros += 1
        for i in range(lastNoneZeros, len(nums)):
            nums[i] = 0
        return nums

solution = Solution()
nums = [0,1,0,3,12]
print(nums)
print(solution.moveZeroes(nums))
nums = [0,1]
print(nums)
print(solution.moveZeroes(nums))
nums = [0,1,0]
print(nums)
print(solution.moveZeroes(nums))
nums = [4,2,4,0,0,3,0,5,1,0]
#[4,2,4,3,5,1,0,0,0,0]
print(nums)
print(solution.moveZeroes(nums))