"""
问题：
字符串数组排序，第二个元素为数字的保留顺序，第二个元素为字母的，按字典序排列

解法：
先把数字移到后面，再对字母的排序
"""
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        words = [i.split() for i in logs]
        cnt = 0
        for i in range(len(words)-1,-1,-1):
            if words[i][1][0].isdigit():
                tmp = words[i]
                words[i] = words[len(words)-cnt-1]
                words[len(words)-cnt-1] = tmp
                cnt+=1
                #print ("swatch str",i)
        #print(words)
        letter_logs_lens = len(words) - cnt
        for i in range(letter_logs_lens):
            for j in range(letter_logs_lens - 1):
                str1 = " ".join(k for k in words[j][1:])
                str2 = " ".join(k for k in words[j+1][1:])
                print(str1,str2)
                if str1 > str2:
                    tmp = words[j]
                    words[j] = words[j+1]
                    words[j+1] = tmp
        return [" ".join(j for j in i) for i in words]

a = "m|w"
b = "mo"
if a > b:
    print("right")
else:
    print("wrong")
solution = Solution()
print(solution.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
#["1 n u","r 527","j 893","6 14","6 82"]
print(solution.reorderLogFiles(["1 n u", "r 527", "j 893", "6 14", "6 82"]))
#["5 m w","j mo","t q h","g 07","o 2 0"]
print(solution.reorderLogFiles(["j mo", "5 m w", "g 07", "o 2 0", "t q h"]))