"""
问题：
给定一个非负整数num，重复地将其每位数字相加，直到结果只有一位数为止。
例如：
给定 num = 38，过程像这样：3 + 8 = 11, 1 + 1 = 2。因为2只有一位，返回之

解法：

(1)依次循环即可
(2)
根据提示，由于结果只有一位数，因此其可能的数字为0 - 9

使用方法I的代码循环输出0 - 19的运行结果：

in  out  in  out
0   0    10  1
1   1    11  2
2   2    12  3
3   3    13  4
4   4    14  5
5   5    15  6
6   6    16  7
7   7    17  8
8   8    18  9
9   9    19  1
可以发现输出与输入的关系为：

out = (in - 1) % 9 + 1
public int addDigits(int num) {
    return (num - 1)%9 + 1;
}
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        strList = [c for c in str(num)]
        while len(strList) > 1:
            total = 0
            for c in strList:
                total += int(c)
            strList = [c for c in str(total)]
        return int(strList[0])

solution = Solution()
num = 38
print (num)
print (solution.addDigits(num))