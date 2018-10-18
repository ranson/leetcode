"""
问题:
在一排树中，第 i 棵树产生 tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：

把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
用这个程序你能收集的水果总量是多少？


解法:
这题其实要求其实很简单，就是找出数组中长度最大的连续由2种元素构成的子数组，返回这个子数组的长度。但由于本题有时间限制，只是朴素的解法会出现超时的情况，需要对实现进行一定的优化。
"""
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        def getCurMax(tree,i,curSet):
            total = 0
            for n in tree[i::-1]:
                if n in curSet:
                    total += 1
                else:
                    return total
            return total

        curMax = 0
        totalMax = 0
        curSet = []
        preTotal = 0
        for i,n in enumerate(tree):
            if n not in curSet:
                if len(curSet) < 2:
                    curSet.append(n)
                    curMax += 1
                else:
                    curSet = []
                    curSet.append(tree[i-1])
                    curSet.append(n)
                    curMax = preTotal + 1
            else:
                curMax += 1
            #print (curSet,totalMax)
            totalMax = max(totalMax,curMax)
            pre = tree[i -1] if i > 0 else tree[i]
            if pre == tree[i]:
                preTotal += 1
            else:
                preTotal = 1
        return totalMax

solution = Solution()
tree = [1,2,1]
print (tree)
print (solution.totalFruit(tree))

tree = [0,1,2,2]
print (tree)
print (solution.totalFruit(tree))

tree = [1,2,3,2,2]
print (tree)
print (solution.totalFruit(tree))

tree = [3,3,3,1,2,1,1,2,3,3,4]
print (tree)
print (solution.totalFruit(tree))

tree = [4,1,1,1,3,1,7,5]
print (tree)
print (solution.totalFruit(tree))

tree = [1,1,6,5,6,6,1,1,1,1]
print (tree)
print (solution.totalFruit(tree))
