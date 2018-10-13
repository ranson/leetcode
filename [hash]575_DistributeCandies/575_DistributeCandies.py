"""
问题：
给定一组长度为偶数的整数，其中每个数字代表一个糖果的种类标号。
将糖果均分给哥哥和妹妹，返回妹妹可以得到的最大糖果种类数。

解法：
返回 min( 糖果总数的一半, 糖果种类数 ) 即可
"""
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = set(candies)
        num = len(candies) // 2
        return num if num < len(kinds) else len(kinds)

solution = Solution()
print(solution.distributeCandies([1,1,2,2,3,3]))
print(solution.distributeCandies([1,1,2,3]))