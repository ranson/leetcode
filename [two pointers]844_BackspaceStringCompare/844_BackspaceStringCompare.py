"""
问题：
给定字符串S和T，其中的#表示退格
求S是否和T相等

解法：
使用栈
"""
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def getStr(s):
            res = []
            for c in s:
                if c == "#":
                    if len(res) > 0:
                        res.pop(len(res)-1)
                else:
                    res.append(c)
            return "".join(res)
        return getStr(S) == getStr(T)

solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))
print(solution.backspaceCompare("ab##", "c#d#"))
print(solution.backspaceCompare("a##c", "#a#c"))
print(solution.backspaceCompare("a#c", "b"))