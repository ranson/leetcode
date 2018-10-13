"""
问题：
给定两个字符串s和t，都只包含小写字母。
字符串t由字符串s打乱顺序并且额外在随机位置添加一个字母组成。
寻找t中新增的那个字母。
测试用例如题目描述。

解法：
分别统计s与t的字母个数，然后比对即可。若使用Python解题，可以使用collections.Counter。

"""
import collections
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = collections.Counter([c for c in s])
        s2 = collections.Counter([c for c in t])
        #print (s2 - s1)
        return "".join(list(s2-s1))

solution = Solution()
print(solution.findTheDifference("abcd","abcde"))