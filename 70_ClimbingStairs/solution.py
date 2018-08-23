class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #for not excced the array when input is 1
        array = [0] * (n+2)
        array[1] = 1
        array[2] = 2
        def getNum(n,array):
            if n > 2:
                return array[n-1] + array[n-2]
            else:
                return array[n]
        for i in range(1,n+1):
            array[i] = getNum(i,array)
        return array[n]

solution = Solution()
cnt = 1
out = solution.climbStairs(cnt)

print("cnt: out:",cnt,out)
