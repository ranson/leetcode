"""
问题：
给定一组有序的字母letters，从中寻找大于字母target的最小字母，（环形有序，z < a）
解法：
二分查找
"""
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        s = 0
        e = len(letters) - 1
        if ord(target) >= ord(letters[e]):
            return letters[0]
        while (s <= e):
            m = (s + e)//2
            if ord(letters[m]) > ord(target):
                e = m - 1
            else:
                s = m + 1
        return letters[s]

solution = Solution()

print(solution.nextGreatestLetter(["c", "f", "j"], "a"))
print(solution.nextGreatestLetter(["c", "f", "j"], "c"))
print(solution.nextGreatestLetter(["c", "f", "j"], "d"))
print(solution.nextGreatestLetter(["c", "f", "j"], "g"))
print(solution.nextGreatestLetter(["c", "f", "j"], "j"))
print(solution.nextGreatestLetter(["c", "f", "j"], "k"))

print(solution.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"],"e"))
