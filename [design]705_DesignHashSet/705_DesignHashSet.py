"""
问题：
构建集合

解法：
使用二分查找
"""
class MyHashSet(object):
    def find_data(self, numsList, key):
        if len(numsList) == 0:
            return 0
        l, r = 0, len(numsList)
        m = 0
        while l < r:
            m = (l + r) // 2
            if numsList[m] == key:
                return m
            elif numsList[m] > key:
                r = m
            else:
                l = m + 1
        return l

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = self.find_data(self.data,key)
        if index < len(self.data) and self.data[index] == key:
            return
        self.data.insert(index,key)


    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = self.find_data(self.data,key)
        if index < len(self.data) and self.data[index] == key:
            self.data.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = self.find_data(self.data,key)
        if index < len(self.data) and self.data[index] == key:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))    #returns true
print(hashSet.contains(3))    #returns false (not found)
hashSet.add(2)
print(hashSet.contains(2))    #returns true
hashSet.remove(2)
print(hashSet.contains(2))    #returns false (already removed)
for i in [72,91,48,41,96,87,48,49,84,82,24,7,56,87,81,55,19,40,68,23]:
    hashSet.add(i)