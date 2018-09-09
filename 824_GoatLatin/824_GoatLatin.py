"""
问题：
如果单词首字母是元音，在单词末尾添加ma
否则，将单词首字母移动至末尾，并添加ma
对于第i个单词，在其末尾添加i个a

解法：
根据题目意思写代码即可。。。
"""
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = set(['a','e','i','o','u','A','E','I','O','U'])

        res = S.split(' ')
        for i,str in enumerate(res):
            if str[0] in vowel:
                res[i] += "ma"
            else:
                res[i] = str[1:] + str[0] + "ma"
            res[i] += 'a' * (i+1)
        return " ".join(res)

solution = Solution()
S = "I speak Goat Latin"
print(S)
print(solution.toGoatLatin(S))
S = "The quick brown fox jumped over the lazy dog"
print(S)
print(solution.toGoatLatin(S))