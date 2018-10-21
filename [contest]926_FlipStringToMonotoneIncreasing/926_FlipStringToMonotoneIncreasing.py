
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        t1 = [0] * len(S)
        t2 = [0] * len(S)
        lcnt = [t1,t2]
        for i,c in enumerate(S):
            val = int(c)
            lcnt[val][i] = lcnt[val][i-1] + 1
            lcnt[val-1][i] = lcnt[val-1][i - 1]
        minimum = min(lcnt[1][len(S)-1],lcnt[0][len(S)-1])
        #print(lcnt)
        for i in range(len(S)-1):
            val = lcnt[1][i]
            val += lcnt[0][len(S)-1] - lcnt[0][i+1]
            #print(val)
            if val < minimum:
                minimum = val
        return minimum

solution = Solution()
print("result:",solution.minFlipsMonoIncr("00110"))
print("result:",solution.minFlipsMonoIncr("010110"))
print("result:",solution.minFlipsMonoIncr("00011000"))
print("result:",solution.minFlipsMonoIncr("11011"))