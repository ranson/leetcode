"""
问题：
给出一组字符串，找出这组字符串可以翻译为多少种不同的morse串
解法：
翻译过来用集合计数即可
"""
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        m = set()
        for word in words:
            res = ""
            for ch in word:
                res += morse[ord(ch) - ord('a')]
            if res not in m:
                m.add(res)
            #print (res)
        return len(m)

solution = Solution()
words = ["gin", "zen", "gig", "msg"]
print (words)
print (solution.uniqueMorseRepresentations(words))