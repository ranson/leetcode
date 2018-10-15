"""
问题：
从升序序列中，查找两个元素，使得其和为target

解法：
依次取元素为index1,二分查找(target - num[index1])即可
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx1 in range(len(numbers) - 1):
            s = idx1 + 1
            e = len(numbers)-1
            while (s <= e):
                m = (s+e)//2
                print (s,e,m)
                if numbers[m] + numbers[idx1] == target:
                    return [idx1+1, m+1]
                elif numbers[m] < target - numbers[idx1]:
                    s = m + 1
                else:
                    e = m -1
        return

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([2,7,11,15], 17))
print(solution.twoSum([2,7,11,15], 13))
print(solution.twoSum([5,25,75], 100))