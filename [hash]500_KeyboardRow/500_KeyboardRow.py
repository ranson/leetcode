"""
问题：
给定一组单词，返回可以用美式键盘中的某一行字母键入的所有单词。
解法：
使用set元素的比较:
s >= t
测试是否 t 中的每一个元素都在 s 中

any 关键字
class Solution(object):
    def findWords(self, words):
        rs = map(set, ['qwertyuiop','asdfghjkl','zxcvbnm'])
        ans = []
        for word in words:
            wset = set(word.lower())
            if any(wset <= rset for rset in rs):
                ans.append(word)
        return ans
"""

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s = [ set(list('qwertyuiop')), set(list('asdfghjkl')), set(list('zxcvbnm'))]
        ret = []
        for w in words:
            for i in s:
                cnt = 0
                for ch in w.lower():
                    if ch in i:
                        cnt += 1
                if cnt == len(w):
                    ret.append(w)
                    break
                elif cnt > 0:
                    break
        return ret

solution = Solution()
print (solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))