"""
问题：
实现棒球记分牌。输入一组字符串：

数字表示分数
'+'表示当前轮次的分数等于上两轮分数之和
'D'表示当前轮次的分数等于上一轮分数加倍
'C'表示清除上一次的分数
求最终的得分总和

解法：
使用栈来记录每一次的得分
"""
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for c in ops:
            if c == "C":
                if len(stack) > 0:
                    stack.pop(0)
            elif c == "D":
                val = stack[0] * 2
                stack.insert(0,val)
            elif c == "+":
                if len(stack) >= 2:
                    val = stack[0] + stack[1]
                    stack.insert(0,val)
            else:
                val = int(c)
                stack.insert(0,val)
        return sum(c for c in stack)

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))
print(solution.calPoints(["5","-2","4","C","D","9","+","+"]))