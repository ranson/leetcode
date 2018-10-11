"""
问题：
如果一个词在一句话中只出现了一次，在另外一句话中没出现，那么这个词是不同的词。找出两句话中所有不同的词。
解法：
统计所有单词出现的次数，次数为一次的就是所求的集合的成员
"""
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        cntSet = {}
        res = set()
        for word in A.split():
            cntSet[word] = cntSet.get(word, 0) + 1
        for word in B.split():
            cntSet[word] = cntSet.get(word, 0) + 1
        for word in cntSet.keys():
            if cntSet[word] == 1:
                res.add(word)
        return list(res)

solution = Solution()
#['sour', 'sweet']
print(solution.uncommonFromSentences("this apple is sweet","this apple is sour"))
#['banana']
print(solution.uncommonFromSentences("apple apple", "banana"))
#['ejt']
print(solution.uncommonFromSentences("s z z z s", "s z ejt"))
#['ta', 'x', 'ft', 'jko', 'yynk', 'lv']
print(solution.uncommonFromSentences("xfj vcahm vcahm frkqt oibcc jko oibcc frkqt ft tr"
,"lv ktx ktx tr x xfj xfj frkqt ktx ta tr yynk vcahm"))