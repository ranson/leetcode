"""
问题：
将数字翻转180度，0, 1, 8会保持原状, 2和5会互换，6和9会互换，其余数字无法翻转。

求1 ~ N中，所有数位均可以翻转，并且翻转后与原数字不同的数字的个数。

解法：
居然是暴力搜索。。。
"""

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        rDig = {'0','1','2','5','6','8','9'}
        rDig2 = {'0','1','8'}
        total = 0
        for i in range(N+1):
            num = str(i)
            isRotated = False
            for c in num:
                if c not in rDig:
                    #print("sip",i)
                    isRotated = False
                    break
                if c not in rDig2:
                    isRotated = True
            if isRotated:
                #print("sip", i)
                total += 1

        return total

solution = Solution()
N = 20
print(N)
print(solution.rotatedDigits(N))
N = 857
print(N)
#247
print(solution.rotatedDigits(N))