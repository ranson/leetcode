"""
问题：
题目大意：
如果整数1到N的排列，第i个数满足下列规则之一，则称该排列为“美丽排列”

第i个位置的数字可以被i整除
i可以被第i个位置的数字整除
给定数字N，求有多少个美丽排列

注意：N是正整数并且不超过15

解法：
回溯法
搜索函数定义为：solve(idx, nums)
其中idx为当前数字的下标，nums为剩余待选数字
初始令idx = 1, nums = [1 .. N]
遍历nums，记当前数字为n，除n以外的其余元素为nums'
若n满足题设的整除条件，则将solve(idx + 1, nums')累加至答案
"""
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        bits = [0] * (N+1)
        def getCnt(pos,N):
            if pos > N:
                return 1
            n = 0
            for i in range(1,N+1):
                if bits[i] == 0:
                    if pos % i == 0 or i % pos == 0:
                        bits[i] = 1
                        n += getCnt(pos+1,N)
                        bits[i] = 0

            return n
        return getCnt(1,N)

solution = Solution()
#print(solution.countArrangement(2))
print(solution.countArrangement(15))