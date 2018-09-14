"""
问题：
1，罗马数字计数规则：

a. 若干相同数字连写表示的数是这些罗马数字的和，如 III=3；
b. 小数字在大数字前面表示的数是用大数字减去小数字，如 IV＝4；
c. 小数字在大数字后面表示的数是用大数字加上小数字，如 VI=6;

其中每两个阶段的之间有一个减法的表示，比如 900=CM， C 写在 M 前面表示 M-C。

2，组合规则：
(1) 基本数字 Ⅰ、X 、C 中的任何一个，自身连用构成数目，或者放在大数的右边连用构成数目，都不能超过三个；放在大数的左边只能用一个。
(2) 不能把基本数字 V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目，只能使用一个。
(3) V 和 X 左边的小数字只能用 Ⅰ。
(4)L 和 C 左边的小数字只能用 ×。
(5)D 和 M 左 边的小数字只能用 C 。

还有一点需要格外注意 MCM是1900
MCMXCVI是1996 也就是按照逻辑 遍历到C 的处理，MC先M+C，但是遍历到第二个M的时候，顺序是CM，这个时候要减去这个C以及之前多加的C，也就是减去两个C。

3，罗马字符
I 1

V 5

X 10

L 50

C 100

D 500

M 1000
解法：
做个字典就好了。。。
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900,
                  "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
                  }
        i = 0
        total = 0
        while (i < len(s)):
            if s[i:i+2] in values.keys():
                total += values[s[i:i+2]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        #values.get()
        return total

solution = Solution()
s = "III"
print (s)
print(solution.romanToInt(s))

s = "IV"
print (s)
print(solution.romanToInt(s))

s = "IX"
print (s)
print(solution.romanToInt(s))

s = "LVIII"
print (s)
print(solution.romanToInt(s))

s = "MCMXCIV"
print (s)
print(solution.romanToInt(s))