"""
问题：
假设你是一位很赞的家长想要给孩子一些饼干。但是，你只能至多给每个孩子一个饼干。孩子i的贪婪因子为gi，意思是他所满意的饼干的最小尺寸；
每一个饼干j的尺寸为sj。如果sj >= gi，我们就可以把饼干j分给孩子i，然后孩子i会很满意。你的目标是最大化分到饼干的孩子的个数。

解法：
首先对贪婪系数g、饼干尺寸s从小到大排序

令指针i指向g的末尾，指针j指向s的末尾

当g和s均≥0时，执行循环：

  若g[i] ≤ s[j] 则令计数器+1，并令j -= 1 （将j号饼干分配给i号孩子，并令j指向下一个更小的饼干）

  令i -= 1 （将i指向下一个贪婪系数更小的孩子）
"""
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        gi, si = 0, 0
        num = 0
        while (gi < len(g) and si < len(s)):
            if s[si] >= g[gi]:
                si += 1
                gi += 1
                num += 1
            else:
                si += 1
        return num

solution = Solution()
print(solution.findContentChildren([1,2,3], [1,1]))
print(solution.findContentChildren([1,2], [1,2,3]))