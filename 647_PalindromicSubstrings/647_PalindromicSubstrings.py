class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """


solution = Solution()
piles = "abc"
print(solution.countSubstrings(piles))
piles = "aaa"
print(solution.countSubstrings(piles))
piles = "noon"
print(solution.countSubstrings(piles))