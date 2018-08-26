"""
问题：
给定一个数组，求指定区域的和

解法：
根据线段树，将查询区间拆分成两个区域，然后从线段树里面查找匹配的区域，线段树的节点（w）里面存储了该节点的子树的和。
所以将找到的区域求和即可。
   [0,5]
|       \
[0,2]   [3,5]
|    \   |   \
[0,1][2][3,4][5]
|   \   | \
[0][1][3][4]
"""
class NumArray(object):

    def __init__(self, a):
        self._n = len(a)
        self._tree = [0] * 4 * self._n
        self._build_tree(a, 0, self._n - 1, 0)

    def _build_tree(self, a, lo, hi, w):
        if lo == hi:
            print ("node ",w,lo,a[lo])
            self._tree[w] = a[lo]
        elif lo < hi:
            mid = lo + (hi - lo) // 2
            self._build_tree(a, lo, mid, 2 * w + 1)
            self._build_tree(a, mid + 1, hi, 2 * w + 2)
            self._tree[w] = self._tree[2 * w + 1] + self._tree[2 * w + 2]
            print("innode ",w,self._tree[w])

    def sumRange(self, i, j):
        return self._sum_range(i, j, 0, self._n - 1, 0)

    def _sum_range(self, q_lo, q_hi, lo, hi, w):
        if q_lo <= lo and hi <= q_hi:
            return self._tree[w]
        if q_lo > hi or q_hi < lo:
            return 0
        mid = lo + (hi - lo) // 2
        return self._sum_range(q_lo, q_hi, lo, mid, 2 * w + 1) + self._sum_range(q_lo, q_hi, mid + 1, hi, 2 * w + 2)

nums=[-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)
i=0
j=2
print(obj.sumRange(i,j))
i=2
j=5
print(obj.sumRange(i,j))
i=0
j=5
print(obj.sumRange(i,j))