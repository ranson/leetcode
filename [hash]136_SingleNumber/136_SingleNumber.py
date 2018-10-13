"""
问题：
给定一个整数数组，除一个元素只出现一次外，其余各元素均出现两次。找出那个只出现一次的元素。
注意：
你的算法应该满足线性时间复杂度。可以不使用额外的空间完成此题吗？

解法：
对数组元素执行异或运算，最终结果即为所求。
由于异或运算的性质，两个相同数字的亦或等于0，而任意数字与0的亦或都等于它本身。另外，异或运算满足交换律。
a ^ b = (a & !b) || (!a & b)
"""
import collections
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        singles = collections.Counter(nums)
        for word in singles:
            if singles[word] == 1:
                return word
        return 0
"""
        singles = set()
        for n in nums:
            if n in singles:
                singles.discard(n)
            else:
                singles.add(n)
        return singles.pop()

"""
solution = Solution()
print ( solution.singleNumber([2,2,1]) )
print ( solution.singleNumber([4,1,2,1,2]) )