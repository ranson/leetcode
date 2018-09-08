"""
问题：
如果一个字符的奇数位与奇数位之间或偶数位与偶数位之间进行交换可以得到另一个字符串，我们就说这两个字符串是等效的。
现在求一组字符串中，不等效的字符串有多少组。

解法：
根据这一准则，对于任意一个字符串，我们可以分别求出其奇数位和偶数位的部分，然后分别进行排序，再合并，这样就能得到一个special value。
例如 "abcd",奇数位为"bd"，偶数位为“ac”,排序合并后"ac#bd" (#为定界符)。所有special value相同的字符串即为所属于同一个组。
"""

class Solution(object):
    def numSpecialEquivGroups_1(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        strSet = set()
        for i in A:
            str = "".join(sorted(i[0::2])) + "#"
            #print("".join(sorted(i[0::2])))
            if len(i)>1:
                str += "".join(sorted(i[1::2]))
                #print(i[1::2])
            #print (str)
            if str not in strSet:
                strSet.add(str)
        return len(strSet)
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def count(str):
            c = [0] * 52
            for i in range(len(str)):
                c[ord(str[i])-ord('a')+26*(i%2)] += 1
            return tuple(c)
        return len({count(i) for i in A})


solution = Solution()
A = ["a","b","c","a","c","c"]
print(A)
print(solution.numSpecialEquivGroups(A))

A = ["aa","bb","ab","ba"]
print(A)
print(solution.numSpecialEquivGroups(A))

A = ["abc","acb","bac","bca","cab","cba"]
print(A)
print(solution.numSpecialEquivGroups(A))

A = ["abcd","cdab","adcb","cbad"]
print(A)
print(solution.numSpecialEquivGroups(A))

A = ["abcd"]
print(A)
print(solution.numSpecialEquivGroups(A))

for i,ch in enumerate(list(A)):
    print(i,ch)