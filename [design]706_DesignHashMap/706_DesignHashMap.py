"""
问题：
设计hashmap

解法：
增加了集合来加速，不然会超时，其实可以排序解决。。。
"""
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []
        self.values = []
        self.setkeys = set()

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.setkeys:
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    self.values[i] = value
                    return
        self.keys.append(key)
        self.values.append(value)
        self.setkeys.add(key)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.setkeys:
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    return self.values[i]
        return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        if key in self.setkeys:
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    self.keys.pop(i)
                    self.values.pop(i)
                    self.setkeys.remove(key)
                    return

hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))             #returns 1
print(hashMap.get(3))           #returns -1 (not found)
hashMap.put(2, 1)         #update the existing value
print(hashMap.get(2))            #returns 1
hashMap.remove(2)         #remove the mapping for 2
print(hashMap.get(2))            #returns -1 (not found)