"""
问题：
检查括号是否匹配

解法：
使用栈即可
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dmap = {")":"(","]":"[","}":"{"}
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.insert(0,c)
            else:
                if stack:
                    if stack.pop(0) != dmap[c]:
                        return False
                else:
                    return False
        return True if len(stack) == 0 else False

solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([)]"))
print(solution.isValid("{[]}"))
