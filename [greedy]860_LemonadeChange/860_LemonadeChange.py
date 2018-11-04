"""
问题：
题目大意:卖lemon，5块钱一个，现在有3种面值的钞票分别为10，20，5，开始的时候没有找零的钱，问能否让每个人都有找零。

解法：
注意20的找零方式一定是先找10的，再找5的，这个地方是greedy算法的体现，因为5的用的多，需要尽量留更多的5在手里。
模拟，注意顺序不能变。
"""
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        inhand = [0,0,0]
        for i in bills:
            if i == 5:
                inhand[0] += 1
            elif i == 10:
                inhand[1] += 1
                inhand[0] -= 1
                if inhand[0] < 0:
                    return False
            elif i == 20:
                inhand[2] += 1
                if inhand[0] >= 1 and inhand[1] >= 1:
                    inhand[0] -= 1
                    inhand[1] -= 1
                else:
                    if inhand[0] < 3:
                        return False
                    else:
                        inhand[0] -= 3
        return True

solution = Solution()
print(solution.lemonadeChange([5,5,5,10,20]))
print(solution.lemonadeChange([5,5,10]))
print(solution.lemonadeChange([10,10]))
print(solution.lemonadeChange([5,5,10,10,20]))
print(solution.lemonadeChange([5,5,5,10,5,5,10,20,20,20]))
