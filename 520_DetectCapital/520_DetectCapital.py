"""
问题：
判断单词是否为首字母大写、全部大写或者全部小写

解法：
按字母意思写代码即可
"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        upperCnt = 0
        isUpper = False
        if word[0].upper() == word[0]:
            isUpper = True
        for i in word:
            if i.upper() == i:
                upperCnt += 1
        if upperCnt == len(word) or upperCnt == 0:
            return True
        if isUpper and  upperCnt == 1:
            return True
        return False

solution = Solution()
word = "USA"
print(word)
print(solution.detectCapitalUse(word))
word = "FlaG"
print(word)
print(solution.detectCapitalUse(word))