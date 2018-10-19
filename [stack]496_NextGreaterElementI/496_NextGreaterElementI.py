"""
问题：
给定两个数组（无重复）nums1 与 nums2，其中nums1的元素是nums2的子集。在nums2中寻找大于nums1中对应位置且距离最近的元素。如果对应位置不存在这样的元素，则输出-1。

注意：

nums1与nums2中的所有元素都是唯一的。
nums1与nums2的元素个数不超过1000。

解法：
使用栈，
将nums压入栈中，当遇到新的数比栈顶的数大时，会弹栈直到不满足条件，并记录该元素对应的比它大的元素（放到map中）
最后检测findNums的元素是否在该map中
"""

import pprint
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dmap = {}
        stack = []
        if stack:
            print ("hhhhh")
        for n in nums:
            while stack and stack[-1] < n:
                pprint.pprint(stack)
                pprint.pprint(dmap)
                dmap[stack.pop()] = n
                pprint.pprint(stack)
                pprint.pprint(dmap)
                print("element:",n)
            stack.append(n)
        return [dmap.get(n, -1) for n in findNums]

solution = Solution()
#print(solution.nextGreaterElement([4,1,2], [1,3,4,2]))
#print(solution.nextGreaterElement([2,4], [1,2,3,4]))
print(solution.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
