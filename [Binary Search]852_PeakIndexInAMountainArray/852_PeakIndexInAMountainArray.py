"""
问题：
找出一个数组中的山峰的索引。山峰的意思是指在一个长度大于3的数组中，某个数值比相邻的两个数值都大。

解法：
这个比普通二叉搜索的改进地方就是不再判断left, mid, right三者之间的关系。
而是对于中间的mid，去判断mid和其相邻的两个元素的关系。根据是否符合山峰的上坡和下坡，去移动指针。

Notice:
if m + 1 < len(A):的条件可以移除，因为不会出现越界的情况，简化出如下代码：
class Solution(object):
    def peakIndexInMountainArray(self, A):
        s,m = 0,0
        e = len(A) - 1
        while(s < e):
            m = (s + e)//2
            if A[m+1] > A[m]:
                s = m+1
            else:
                e = m

        return s
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s, m = 0, 0
        e = len(A) - 1
        while (s < e):
            m = (s + e) // 2
            if A[m + 1] > A[m]:
                s = m + 1
            else:
                e = m
        return s
        """
        s,m = 0,0
        e = len(A) - 1
        while(s < e):
            m = (s + e)//2
            #print (s,e,m)
            if m + 1 < len(A):#remove it, unnecessary
                if A[m+1] > A[m]:
                    s = m+1
                else:
                    e = m
            else:
                if A[m-1] > A[m]:
                    e = m-1
                else:
                    s = m
        return s if A[s] > A[e] else e
        """
solution = Solution()
print(solution.peakIndexInMountainArray([0,1,0]))
print(solution.peakIndexInMountainArray([0,2,1,0]))
print(solution.peakIndexInMountainArray([0,1,2,3,4]))