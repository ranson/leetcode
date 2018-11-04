"""
问题：
给定一个唯一数字的集合，返回所有可能的排列

解法：
解法一：
使用回溯法：记录未访问的元素，逐个构造所有位置的元素

解法二：
递归（Recursion）

记传入数组为nums，若nums的长度不大于1，则直接返回[nums]

遍历nums，从中抽取一个数num，递归计算剩余数字组成的数组n，然后将num与结果合并
class Solution(object):
    def permute(self, nums):
        if len(nums) <= 1: return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for y in self.permute(n):
                ans.append([num] + y)
        return ans
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visit = set(nums)
        result = []
        n = [0] * len(nums)
        def getPermute(nums, pos, visit, result,n):
            toVisited = [i for i in visit]
            for i in toVisited:
                visit.remove(i)
                n[pos] = i
                if pos < len(nums) - 1:
                    #print("visited ", i)
                    getPermute(nums,pos+1,visit,result,n)
                else:
                    #print ("append ",n)
                    result.append([i for i in n])
                visit.add(i)
        getPermute(nums,0,visit,result,n)
        return result

solution = Solution()
print(solution.permute([8,2,-1,6]))