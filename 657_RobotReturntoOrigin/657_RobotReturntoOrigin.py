"""
问题：
从(0,0)点出发，U表示向上，D表示向下，L表示向左，R表示向右，判断是否回到原点
解法：
其实只要保持两个坐标就行，x坐标与y坐标
"""
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        step = {"L":0,"R":0,"U":0,"D":0}
        for i in moves:
            step[i] = step[i] + 1
        if step["U"] == step["D"] and step["L"] == step["R"]:
            return True
        return False

solution = Solution()
moves = "UD"
print(moves)
print(solution.judgeCircle(moves))
moves = "LL"
print(moves)
print(solution.judgeCircle(moves))