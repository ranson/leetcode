"""
问题：
给定目标字符串licensePlate以及字符串数组words。
在words中寻找可以覆盖licensePlate中的所有字母的最小下标对应的单词。

解法：
字符串处理
将licensePlate转化为小写，正则表达式删除所有非字母字符，并逐字母统计个数。
遍历words
"""
import collections
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        plate = {}
        res = ""
        for w in licensePlate.lower() :
            if w.isalpha():
                plate[w] = plate.get(w, 0) + 1
        #print ("plate:",plate)
        for w in words:
            cnt = collections.Counter([c for c in w])
            #print ("cnt:",cnt)
            flag = True
            for k in plate.keys():
                #print("this is plat key:",k, cnt[k] , plate[k])
                if not (k in set(cnt) and cnt[k] >= plate[k]):
                    flag = False
                    break
            if flag:
                if len(res) == 0 or len(w) < len(res):
                    res = w
        return res

solution = Solution()
print (solution.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]))
print (solution.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]))