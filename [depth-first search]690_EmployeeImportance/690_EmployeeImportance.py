"""
问题：
给定一组雇员信息，包含ID，影响力，直接下属的ID列表。
求某雇员及其所有下属的影响力之和。

解法：
递归
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates



class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emap = {e.id:e for e in employees}
        def dfs(subid):
            employee = emap[subid]
            return (employee.importance + sum(dfs(e) for e in employee.subordinates))
        return dfs(id)

l = list()
l.append(Employee(1,5,[2,3]))
l.append(Employee(2, 3, []))
l.append(Employee(3, 3, []))
solution = Solution()
print(solution.getImportance(l,1))