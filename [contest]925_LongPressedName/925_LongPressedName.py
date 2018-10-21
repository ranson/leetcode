class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if not(name):
            if not(typed):
                return True
            else:
                return False
        def getCnts(s):
            if not(s):
                return []
            cnts = []
            lastch = s[0]
            cnt = 0
            for c in s:
                if c == lastch:
                    cnt += 1
                else:
                    cnts.append((c,cnt))
                    cnt = 1
                    lastch = c
            cnts.append((s[-1], cnt))
            return cnts
        a = getCnts(name)
        b = getCnts(typed)
        if len(a) == len(b) and all(a[i][0] == b[i][0] and b[i][1] >= a[i][1] for i in range(len(a))):
            return True
        else:
            return False

solution = Solution()
print(solution.isLongPressedName( "alex", "aaleex"))
print(solution.isLongPressedName( "saeed", "ssaaedd"))
print(solution.isLongPressedName( "leelee", "lleeelee"))
print(solution.isLongPressedName( "laiden", "laiden"))