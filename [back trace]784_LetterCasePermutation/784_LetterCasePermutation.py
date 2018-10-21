"""
问题：
给定字符串S，将其中的字母分别转化为大、小写，求所有组合。

解法：
直接循环求即可。。。
递归也可以：
class Solution(object):
    def letterCasePermutation(self, S):
        if not S: return [S]
        rest = self.letterCasePermutation(S[1:])
        if S[0].isalpha():
            return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]
        return [S[0] + s for s in rest]
"""
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for c in S:
            appendCh = []
            if c.isdigit():
                appendCh.append(c)
            else:
                appendCh.append(c.lower())
                appendCh.append(c.upper())
            nlist = []
            for apd in appendCh:
                if res:
                    for letter in res:
                        nlist.append(letter + apd)
                else:
                    nlist.append(apd)
            res = nlist
        return res

solution = Solution()
print(solution.letterCasePermutation("a1b2"))
print(solution.letterCasePermutation("3z4"))
print(solution.letterCasePermutation("12345"))
print(solution.letterCasePermutation(""))
print(solution.letterCasePermutation("abcd"))