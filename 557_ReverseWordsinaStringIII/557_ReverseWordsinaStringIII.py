"""
问题：
单词倒序，句子不倒序
解法：
使用python的string的操作很简单。。。

一行python搞定。。。
return " ".join([i[::-1] for i in s.split()])
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        start = -1
        for i in range(len(s)):
            if s[i] == ' ':
                res += s[i-1:start:-1] if start >= 0 else s[i-1::-1]
                res += ' '
                start = i
        res += s[len(s) - 1:start:-1] if start >= 0 else s[len(s)-1::-1]
        return res

solution = Solution()
s = "Let's take LeetCode contest"
print(s)
print (solution.reverseWords(s))
s = "contest"
print(s)
print (solution.reverseWords(s))